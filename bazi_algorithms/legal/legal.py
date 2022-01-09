"""Logged-in page routes."""
from flask import Blueprint, render_template

# Blueprint Configuration
legal_bp = Blueprint(
    'legal_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@legal_bp.route('/privacy-policy', methods=['GET'])
def privacy():
    return render_template(
        'legal.jinja2',
        content='privacy_policy'
    )


@legal_bp.route('/terms-conditions', methods=['GET'])
def terms_and_conditions():
    return render_template(
        'legal.jinja2',
        content='terms_and_conditions'
    )


@legal_bp.route('/terms-of-use', methods=['GET'])
def terms_of_use():
    return render_template(
        'legal.jinja2',
        content='terms_of_use'
    )


@legal_bp.route('/returns-and-refunds', methods=['GET'])
def return_and_refund():
    return render_template(
        'legal.jinja2',
        content='return_and_refund'
    )


@legal_bp.route('/disclaimer', methods=['GET'])
def disclaimer():
    return render_template(
        'legal.jinja2',
        content='disclaimer'
    )


@legal_bp.route('/eula', methods=['GET'])
def eula():
    return render_template(
        'legal.jinja2',
        content='eula'
    )
