import os
from flask_login.utils import login_required
import stripe
import json
#from requests import request
from flask import session, Flask, flash, jsonify, Blueprint, render_template, url_for, redirect, request, abort
from flask_login import current_user
from ..persistence.models import StripeCustomer, User, db
import math
import time
from sqlalchemy import func

# Blueprint Configuration
pay_bp = Blueprint(
    'pay_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

stripe.api_key = os.getenv("STRIPE_API_KEY")

stripe_keys = {
    "secret_key": os.getenv("STRIPE_SECRET_KEY_TEST"),
    "publishable_key": os.getenv("STRIPE_PUBLISHABLE_KEY_TEST"),
    "annual_price_id": os.getenv("STRIPE_ANNUAL_PLAN_PRICE_ID_TEST"), 
    "premium_price_id": os.getenv("STRIPE_PREMIUM_PLAN_PRICE_ID_TEST"), 
    "plus_price_id": os.getenv("STRIPE_PLUS_PLAN_PRICE_ID_TEST"),
    "endpoint_secret": os.getenv("STRIPE_ENDPOINT_SECRET_TEST")
}

plan_dic = {"plusplan" : "plus_price_id", "premiumplan" : "premium_price_id", "annualplan" : "annual_price_id"}

@pay_bp.route("/pay") 
def pay():
    if not current_user.is_authenticated:
      flash("To proceed to Pricing, kindly Log In or Signup.", "info")
      return redirect(url_for("auth_bp.login") + '?next=pay')
    
    if "next" in session.keys():
        session.pop("next")

    return render_template("payment.jinja2")

@pay_bp.route("/stripe_public")
def get_publishable_key():
    stripe_config = {"publicKey": stripe_keys["publishable_key"]}
    return jsonify(stripe_config)

@pay_bp.route("/create-checkout-session/<plan>")
def create_checkout_session(plan):
    """Creates a Stripe session object that populates their intermediary page.
    User has to be logged in to access this route, so that we can track the current_user.id for later use."""
    try:

        checkout_session = stripe.checkout.Session.create(
            client_reference_id=current_user.id,
            success_url= url_for('pay_bp.pay_success', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url= url_for('pay_bp.pay_cancel', _external=True),
            payment_method_types=['card'],
            mode='subscription',
            line_items=[{
                'price': stripe_keys[plan_dic[plan]],
                'quantity': 1
                }],
        )
        return jsonify({'sessionId': checkout_session['id']})
    except Exception as e:
        return jsonify({'error': {'message': str(e)}}), 400

@pay_bp.route("/webhook", methods=["POST"])
def stripe_webhook():
    payload = request.get_data(as_text=True)
    sig_header = request.headers.get("Stripe-Signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, stripe_keys["endpoint_secret"]
        )

    except ValueError as e:
        # Invalid payload
        return "Invalid payload", 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return "Invalid signature", 400

    # Handle the checkout.session.completed event
    if event["type"] == "checkout.session.completed":
        stripe_data = event["data"]["object"]
        handle_checkout_session(stripe_data)

    return "Success", 200

def handle_checkout_session(data):

    if "client_reference_id" in data.keys():
        if data["client_reference_id"] is None:
            user_id = 0
        else:
            user_id = data["client_reference_id"]
    else:
        user_id = 0

    if "customer_details" in data.keys():
        if "email" in data["customer_details"].keys():
            email = data["customer_details"]["email"]
        else:
            email = "no_email"
    else:
        email = "no_email"

    if "payment_status" in data.keys():
        if data["payment_status"] is None:
            payment_status = "no_result"
        else:
            payment_status = data["payment_status"]
    else:
        payment_status = "no_result"

    if "amount_subtotal" in data.keys():
        if data["amount_subtotal"] is None:
            amount_subtotal = 0
        else:
            amount_subtotal = data["amount_subtotal"]/ 100
    else:
        amount_subtotal = 0

    if "amount_total" in data.keys():
        if data["amount_total"] is None:
            amount_total = 0
        else:
            amount_total = data["amount_total"]/ 100
    else:
        amount_total = 0

    if "currency" in data.keys():
        if data["currency"] is None:
            currency = "no_result"
        else:
            currency = data["currency"]
    else:
        currency = "no_result"
        
    if "id" in data.keys():
        if data["id"] is None:
            stripe_session_id = "no_result"
        else:
            stripe_session_id = data["id"]
    else:
        stripe_session_id = "no_result"

    if "customer" in data.keys():
        if data["customer"] is None:
            stripe_customer_id = "no_result"
        else:
            stripe_customer_id = data["customer"]
    else:
        stripe_customer_id = "no_result"

    if "subscription" in data.keys():
        if data["subscription"] is None:
            stripe_subscription_id = "no_result"
        else:
            stripe_subscription_id = data["subscription"]
    else:
        stripe_subscription_id = "no_result"

    date = math.floor(time.time())
    print("date")
    print(date)

    stripe_customer = StripeCustomer(
            user_id=user_id,
            email=email,
            amount_subtotal=amount_subtotal,
            amount_total=amount_total,
            payment_status=payment_status,
            currency=currency,
            date=date,
            stripe_session_id=stripe_session_id,
            stripe_customer_id=stripe_customer_id,
            stripe_subscription_id=stripe_subscription_id
        )

    try:
        db.session.add(stripe_customer)
        db.session.commit() 
    except:
        db.session.rollback()

    if user_id != 0 and payment_status == 'paid':
        # https://testdriven.io/blog/flask-stripe-subscriptions/
        customer = StripeCustomer.query.filter_by(user_id=user_id).order_by(StripeCustomer.date.desc()).first()
        subscription = stripe.Subscription.retrieve(customer.stripe_subscription_id)
        product = stripe.Product.retrieve(subscription.plan.product)

        if "metadata" in product.keys():
            if "plan_name" in product["metadata"].keys():
                user = User.query.filter_by(id=user_id).first() 
                user.plan = product["metadata"]["plan_name"]

                try:
                    db.session.commit() 
                except:
                    db.session.rollback()

@pay_bp.route("/pay_success")
def pay_success():
    return render_template("success.jinja2")

@pay_bp.route("/pay_cancel")
def pay_cancel():
    return render_template("cancel.jinja2")

@pay_bp.errorhandler(500)
def not_found_error(error):
    return render_template('500.jinja2')