from flask import Blueprint, redirect, render_template, url_for, flash, session, request, abort
from flask_login import current_user, login_required
from flask_wtf.csrf import CSRFProtect
from .cache import cache

main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@main_bp.route("/", methods=['GET', 'POST'])
def main():
        return "ok"



