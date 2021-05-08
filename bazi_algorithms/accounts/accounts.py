from flask import Blueprint, redirect, render_template, url_for, flash, session, request, abort
from flask_login import current_user, login_required
from flask_wtf.csrf import CSRFProtect
from ..persistence.models import User, db, Profile
import numpy as np

accounts_bp = Blueprint(
    'accounts_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@accounts_bp.route('/account', methods=['GET'])
@login_required
def account_info():
    """Show User Information"""

    return render_template(
        'accounts.jinja2',
        current_user=current_user,
    )