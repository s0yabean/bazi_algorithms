from flask import Blueprint, redirect, render_template, url_for, flash, session, request, abort
from flask_login import current_user, login_required
from flask_wtf.csrf import CSRFProtect
from .cache import cache
from .forms.chart_form import ChartFormManual, ChartFormBirthTime
from .persistence.models import NatalChart, db, User
import requests
import re
from os import environ

main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@main_bp.route("/home", methods=['GET', 'POST'])
@login_required
def main():
    chart_form = ChartFormManual()
    chart_form_2 = ChartFormBirthTime()

    if request.method == 'POST':
        if chart_form_2.validate_on_submit():

            hour = re.search(r'[0-9]*', chart_form_2.hour_range.data).group()
            birthday = str(chart_form_2.birth_date.data)
            bazi_api_url = environ.get('BAZI_API_URL')
            bazi_url = bazi_api_url.format(chart_form_2.gender.data, birthday[:4], birthday[5:7], birthday[8:11], hour,chart_form_2.hour_range.data[:-2])
            page = requests.get(bazi_url)
            content = str(page.content)

            x = re.search("(?=Day Master)(.*)(?=10 Year)", content)
            y = re.search("(?=<td>)(.*)(</td>)", x[0])
            z = re.sub('<[^<]+?>', '', y[0])
            z = re.sub(r'\\x*[A-z0-9]+', '', z)
            z = z.replace("\\r", "").replace('\\n', "")
            z = re.sub("[ ]+", ' ', z)
            
            hour = re.search("(?=Hour)(.*)(?=Day)", z)[0].split(" ")
            day = re.search("(?=Day)(.*)(?=Month)", z)[0].split(" ")
            month = re.search("(?=Month)(.*)(?=Year)", z)[0].split(" ")
            year = re.search("(?=Year)(.*)", z)[0].split(" ")

            natal_chart = NatalChart(
                user_id = current_user.id,
                contact_name = chart_form_2.name.data,
                hour_s = hour[1],
                hour_e = hour[4],
                day_s = day[1],
                day_e = day[4],
                month_s = month[1],
                month_e = month[4],
                year_s = year[1],
                year_e = year[4],
                self_chart = chart_form_2.my_own_chart_checkbox.data
            )

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
                year_e = chart_form.year_branch.data,
                self_chart = chart_form.my_own_chart_checkbox.data
            )

        chart_validation = NatalChart.query.filter_by(user_id=current_user.id, contact_name=chart_form.name.data).all()
        if len(chart_validation) > 0:
            flash("There is already a user with name " + chart_form.name.data + ". Please change to another name.", "error")
        else:
            try:
                db.session.add(natal_chart)
                db.session.commit() 
                flash("Chart for " + chart_form.name.data + " added. Bazi: " + natal_chart.hour_s + " " + natal_chart.hour_e + ", " + natal_chart.day_s + " " +  natal_chart.day_e + ", " + natal_chart.month_s + " " + natal_chart.month_e + ", " + natal_chart.year_s + " " + natal_chart.year_e, "info")
            except Exception as e: 
                db.session.rollback()
                print(e)
                abort(500)

            if chart_form.my_own_chart_checkbox.data:
                new_natal_chart_id = NatalChart.query.filter_by(user_id=current_user.id, contact_name=chart_form.name.data).one().id
                User.query.filter_by(id=current_user.id).update({"natal_chart_id": new_natal_chart_id})
                db.session.commit() 
                flash("Your personal chart is updated. Bazi: " + natal_chart.hour_s + " " + natal_chart.hour_e + ", " + natal_chart.day_s + " " +  natal_chart.day_e + ", " + natal_chart.month_s + " " + natal_chart.month_e + ", " + natal_chart.year_s + " " + natal_chart.year_e, "info")

    if NatalChart.query.filter_by(id=current_user.natal_chart_id).all() != []:
        user_chart = NatalChart.query.filter_by(id=current_user.natal_chart_id).one()
    else:
        user_chart = None

    return render_template('home.jinja2', 
    current_user = current_user,
    form = chart_form,
    chart_form_birth_time = chart_form_2,
    user_chart = user_chart
    )
