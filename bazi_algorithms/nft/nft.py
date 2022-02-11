"""Logged-in page routes."""
from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required

# Blueprint Configuration
nft_bp = Blueprint(
    'nft_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@nft_bp.route('/nft', methods=['GET'])
def nft():
    return render_template(
        'nft.jinja2',
        title='The BaziVerse NFT Collection on Rarible'
    )

