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
    from .persistence.models import NatalChart, db, User
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

        chart_validation = NatalChart.query.filter_by(user_id=current_user.id, contact_name=chart_form.name.data).all()
        if len(chart_validation) > 0:
            flash("There is already a user with name " + chart_form.name.data + ". Please change to another name.", "error")
        else:
            try:
                db.session.add(natal_chart)
                db.session.commit() 
                flash("Chart for " + chart_form.name.data + " added.", "info")
            except Exception as e: 
                db.session.rollback()
                print(e)
                abort(500)

            if chart_form.my_own_chart_checkbox.data:
                new_natal_chart_id = NatalChart.query.filter_by(user_id=current_user.id, contact_name=chart_form.name.data).one().id
                User.query.filter_by(id=current_user.id).update({"natal_chart_id": new_natal_chart_id})
                db.session.commit() 
                flash("Your personal chart is updated.", "info")

    natal_chart_id = User.query.filter_by(id=current_user.id).one().natal_chart_id
    print(NatalChart.query.filter_by(id=natal_chart_id).all())
    if NatalChart.query.filter_by(id=natal_chart_id).all() != []:
        user_chart = NatalChart.query.filter_by(id=natal_chart_id).one()
    else:
        user_chart = None

    return render_template('home.jinja2', 
    current_user = current_user,
    form = chart_form,
    user_chart = user_chart
    )
