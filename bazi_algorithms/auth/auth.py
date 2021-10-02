"""Routes for user authentication."""
from flask import Blueprint, flash, redirect, render_template, request, url_for, abort
from flask_login import current_user, login_user, login_required, logout_user
from .. import login_manager
from ..forms.auth_forms import LoginForm, SignupForm
from ..persistence.models import User, db
from flask import session

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
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            user = User(
                name=form.name.data,
                email=form.email.data,
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
        user = User.query.filter_by(email=form.email.data).first()  
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
