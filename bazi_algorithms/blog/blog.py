from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required

# Blueprint Configuration
blog_bp = Blueprint(
    'blog_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@blog_bp.route('/clash-vs-combine', methods=['GET'])
def clash_combine_article():
    return render_template(
        'blog.jinja2',
        article='clash_combine_article'
    )

@blog_bp.route('/nobleman', methods=['GET'])
def nobleman_article():
    return render_template(
        'blog.jinja2',
        article='nobleman'
    )

@blog_bp.route('/bazi-does-not-predict-future', methods=['GET'])
def bazi_does_not_predict_future():
    return render_template(
        'blog.jinja2',
        article='bazi_does_not_predict_future'
    )

