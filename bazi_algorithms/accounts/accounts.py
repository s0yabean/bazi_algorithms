from flask import Blueprint, render_template
from flask_login import (current_user,
                         login_required,
                         )

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
