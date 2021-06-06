import os
import stripe
import json
from requests import request
from flask import Flask, jsonify, Blueprint, render_template, url_for

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
    "plus_price_id": os.getenv("STRIPE_PLUS_PLAN_PRICE_ID_TEST")
}

@pay_bp.route("/pay")
def pay():
    return render_template("payment.jinja2")

@pay_bp.route("/stripe_public")
def get_publishable_key():
    stripe_config = {"publicKey": stripe_keys["publishable_key"]}
    return jsonify(stripe_config)

@pay_bp.route("/create-checkout-session")
def create_checkout_session():
  #data = json.loads(request.data)

  try:
    checkout_session = stripe.checkout.Session.create(
      success_url= url_for('pay_bp.pay_success', _external=True) + '?session_id={CHECKOUT_SESSION_ID}',
      cancel_url= url_for('pay_bp.pay_cancel', _external=True),
      payment_method_types=['card'],
      mode='subscription',
      line_items=[{
        'price': stripe_keys['annual_price_id'],
        'quantity': 1
      }],
    )
    return jsonify({'sessionId': checkout_session['id']})
  except Exception as e:
    return jsonify({'error': {'message': str(e)}}), 400

@pay_bp.route("/pay_success")
def pay_success():
    return render_template("success.html")

@pay_bp.route("/pay_cancel")
def pay_cancel():
    return render_template("cancel.html")