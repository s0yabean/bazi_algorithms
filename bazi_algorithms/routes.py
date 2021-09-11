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
    from .forms.chart_form import ChartForm
    from .persistence.models import NatalChart, db
    chart_form = ChartForm()

    if chart_form.validate_on_submit():
        natal_chart = NatalChart(
            user_id = current_user.id,
            contact_name = chart_form.name.data,
            hour_s = chart_form.hour_stem.data,
            hour_e = chart_form.hour_branch.data,
            day_s = chart_form.day_stem.data,
            day_e = chart_form.day_branch.data,
            month_s = chart_form.month_stem.data,
            month_e = chart_form.month_branch.data,
            year_s = chart_form.year_stem.data,
            year_e = chart_form.year_branch.data
        )

        try:
            db.session.add(natal_chart)
            db.session.commit() 
            flash("Chart for " + chart_form.name.data + " added.", "info")
        except Exception as e: 
            db.session.rollback()
            print(e)
            abort(500)

    return render_template('home.jinja2', 
    current_user = current_user,
    form = chart_form
    )
