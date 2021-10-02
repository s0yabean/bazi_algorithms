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
        title="Leverage Your Network's Bazi."
    )

@landing_bp.route('/about', methods=['GET'])
def about_us():
    return render_template(
        'about.jinja2',
        title='Bazi for Modern Age.'
    )

@landing_bp.route('/newsletter', methods=['GET'])
def newsletter():
    return render_template(
        'newsletter.jinja2',
        title='Bazilogy Newsletter.'
    )
