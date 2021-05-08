"""Logged-in page routes."""
from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required

# Blueprint Configuration
demo_bp = Blueprint(
    'demo_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@demo_bp.route('/demo', methods=['GET'])
def demo():
    return render_template(
        'demo.jinja2',
        title='Flask-Login Tutorial.'
    )

