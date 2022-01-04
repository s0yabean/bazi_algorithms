"""Routes for user authentication."""
from email import message
from re import template
from flask import Blueprint, flash, redirect, render_template, request, url_for, abort
from flask_login import current_user, login_user, login_required, logout_user
from .. import login_manager
from ..forms.auth_forms import LoginForm, SignupForm, ForgotPasswordForm, ResetPasswordForm
from ..persistence.models import User, db
from flask import session
from itsdangerous import JSONWebSignatureSerializer as Serializer, exc
from flask_mail import Message
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
# from flaskblog import mail

    
# Blueprint Configuration
auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    User sign-up page.

    GET requests serve sign-up page.
    POST requests validate form & user creation.
    """

    # using sessions for /signup due to SignupForm deleting request.args 
    if request.args.get('next') == 'pay':
        session["next"] = "pay"

    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data.lower()).first()
        if existing_user is None:
            user = User(
                name=form.name.data,
                email=form.email.data.lower(),
                plan="Lite Plan"
            )
            user.set_password(form.password.data)

            try:
                db.session.add(user)
                db.session.commit() 
            except:
                db.session.rollback()
                abort(500)
            
            login_user(user)  # Log in as newly created user

            if "next" in session.keys():
                link = session["next"]
                session.pop("next")
                return redirect(link)
            else:
                return redirect(url_for('main_bp.main'))
        flash('A user already exists with that email address.')

    return render_template(
        'signup_page.jinja2',
        title='Create an Account.',
        form=form,
        template='signup-page',
        body="Sign up for a user account."
    )

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Log-in page for registered users.

    GET requests serve Log-in page.
    POST requests validate and redirect user to /ai page.
    """

    # Bypass if user is logged in
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.main'))  

    form = LoginForm()
    # Validate login attempt
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()  
        if user and user.check_password(password=form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main_bp.main'))
        flash('Invalid username/password combination')
        return redirect(url_for('auth_bp.login'))
    return render_template(
        'login_page.jinja2',
        form=form,
        title='Log in.',
        template='login-page',
        body="Log in with your User account."
    )

@auth_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    from ..persistence.data_utilities import sessions_reset
    logout_user()
    sessions_reset()
    return redirect(url_for('auth_bp.login'))

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in upon page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None

@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You Must Be Logged In To View That Page.')
    return redirect(url_for('auth_bp.login'))

@auth_bp.errorhandler(500)
def not_found_error(error):
    return render_template('500.jinja2')


@auth_bp.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    """
    User forget password page.

    GET requests serve sign-up page.
    POST requests validate form & user creation.
    """
    form = ForgotPasswordForm()
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.main'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()  
        if user:
            send_reset_email(user)
            flash('An email has been sent with instructions to reset your password.', 'info')
            # send_reset_email(user)
            return redirect(url_for('auth_bp.login'))
            # flash('User Exists')
            # flash(form.email)
            # flash(user.id)
            # flash((user.verify_reset_token(user.get_reset_token())).email)
        else:
            flash('Email not registered')
            return redirect(url_for('auth_bp.signup'))

    return render_template(
        'forgot_password_page.jinja2',
        title='Password reset request.',
        form=form,
        template='forgot-password-page',
        body="Reset your password"
    )

def send_reset_email(user):
    recipient = user.email
    port_number = 465
    sender_email = "bazi.backend@gmail.com"
    token = user.get_reset_token()
    app_password = "nyubrygylmnzctdb"
    link = url_for('auth_bp.reset_password', token=token, _external=True)
    body = open("bazi_algorithms/static/src/email_forgot_pw.html","r")
    body = body.read()
    body = body.replace("http://www.example.com",link)
    message = MIMEMultipart('alternative')
    message["Subject"] = Header("Password reset request","utf-8")
    message["From"] = Header(sender_email,"utf-8")
    message["To"] = Header(recipient,"utf-8")
    part1 = MIMEText(body,'html')
    message.attach(part1)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",port_number,context=context) as server:
        server.login(sender_email,app_password)
        server.sendmail(sender_email,recipient,message.as_string())

    # msg = Message('Password Reset Request',
    #               sender='noreply@demo.com',
    #               recipients=[user.email])
    # msg.body = 

    # mail.send(msg)

@auth_bp.route("/reset_password/<token>", methods=['GET', 'POST'])
@auth_bp.route("/reset_password",defaults={'token': None}, methods=['GET', 'POST'])
def reset_password(token):
    
    if token:
        session['token'] = token
        print("        Token :          ")
        print(token)
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.main'))
    user = User.verify_reset_token(token)
    if user is None:
        token = session['token']
        user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token, please request a new one.', 'warning')
        return redirect(url_for('auth_bp.forgot_password'))
    
    form = ResetPasswordForm()

    if form.validate_on_submit():
        user.set_password(form.password.data)
        try:
            db.session.commit()
            # flash('Your password has been updated! Please use your new password to log in.', 'success')
            return render_template('success_changepw_page.jinja2')
        except:
            flash('An error happened , please contact our service team.', 'warning')
            return redirect(url_for('main_bp.main'))
      
    # using sessions for /signup due to SignupForm deleting request.args 
    return render_template('password_reset_page.jinja2',
    title='User Password Reset',
    form=form,
    template='password-reset-page',
    body='Change Password')
