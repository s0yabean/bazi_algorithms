from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required

# Blueprint Configuration
landing_bp = Blueprint(
    'landing_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@landing_bp.route('/', methods=['GET'])
def landing():
    return render_template(
        'landing.jinja2',
        title='MBTI App Demo.'
    )
