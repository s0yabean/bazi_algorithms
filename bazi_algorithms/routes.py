from flask import Blueprint, redirect, render_template, url_for, flash, session, request, abort
from flask_login import current_user, login_required
from flask_wtf.csrf import CSRFProtect
from .cache import cache

main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@main_bp.route("/home", methods=['GET', 'POST'])
@login_required
def main():
    from .forms.date_forms import DateForm
    Dateform = DateForm()
    return render_template('home.jinja2', current_user = current_user,
    form = Dateform)
