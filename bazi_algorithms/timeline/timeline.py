import math
from datetime import date, datetime, timedelta
from flask import (
    Blueprint,
    render_template,
    flash,
    session, 
    request
)
from flask_login import current_user, login_required

import pandas as pd
import numpy as np

from bazi_algorithms.forms.date_forms import TimelineDateForm
from bazi_algorithms.forms.name_forms import ChoiceForm
from bazi_algorithms.persistence.models import NatalChart, ExternalPillars
from bazi_algorithms.bazi_formulas.timeline_scoring import calc_comb_clash

timeline_bp = Blueprint(
    'timeline_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@timeline_bp.route("/timeline", methods=['GET', 'POST'])
@login_required
def main():

    data = [{'s_combine': 0, 's_clash': 0, 'e_combine': 0, 'e_clash': 0}]
    avg_combine = [0] 
    avg_clash = [0]
    window_size = 0
    rolling_data_comb = [0]
    rolling_data_clash = [0]
    chart = None
    dates = ExternalPillars.query.filter(ExternalPillars.date == str(date.today())).all()

    natal_chart_list = list(NatalChart.query.filter_by(user_id=current_user.id).all())

    choice_form = ChoiceForm()
    date_form = TimelineDateForm()

    if 'start_date' not in session.keys():
        session['start_date'] = datetime(int(str(datetime.today())[:4]), 1, 1)
        session['end_date'] = datetime(int(str(datetime.today())[:4]), 12, 31)
        dates = ExternalPillars.query.filter(
                    ExternalPillars.date >= session["start_date"] - timedelta(days=window_size), 
                    ExternalPillars.date <= session["end_date"]
                ).all()

    if request.method == 'GET':
        if current_user.natal_chart_id is None:
            flash("Please add in your own chart in the Account section to see your own chart on default.", "info")
            return render_template('timeline.jinja2', 
                form=date_form,
                user_chart=chart,
                natal_chart=natal_chart_list,
                choice_form=choice_form,
                session=session,

                data=data[window_size:],
                labels=[d.date for d in dates[window_size:]],

                avg_combine=avg_combine,
                avg_clash=avg_clash,

                rolling_data=rolling_data_comb[window_size:],
                rolling_data_clash=rolling_data_clash[window_size:]
            )

        if session.get('contact_chart') is None:
            default_natal_chart = NatalChart.query.filter_by(id=current_user.natal_chart_id).one()
            session['contact_name_id'] = default_natal_chart.id
            session['contact_name'] = default_natal_chart.contact_name

    elif request.method == 'POST':
        if "dropdown_menu" in request.form.keys() and "security_token" in request.form.keys():
            # The value of request.form['security_token'] should probably be validated here
            contact_id = request.form["dropdown_menu"]
            contact_chart = NatalChart.query.filter_by(id=contact_id).one()

            session['contact_name_id'] = contact_id 
            session['contact_name'] = contact_chart.contact_name
            session["contact_chart"] = contact_chart

            date_form.startdate.data = session['start_date']
            date_form.enddate.data = session['end_date']
    
    print("outside form submit")
    if date_form.validate_on_submit():
        print("entered date form")
        print(date_form.startdate.data)
        print(date_form.enddate.data)
        session['start_date'] = date_form.startdate.data
        session['end_date'] = date_form.enddate.data
        print(session['start_date'])
        print(session['end_date'])

    contact_not_present =   'contact_name' not in session.keys() and \
                            'contact_name_id' not in session.keys() 

    if contact_not_present:
        flash("Please Select A Person In The Dropdown Menu.", "info")

    display_chart = 'start_date' in session.keys() and \
                    'end_date' in session.keys() and \
                    session["start_date"] is not None and \
                    session["end_date"] is not None and \
                    not contact_not_present

    if display_chart:

        num_days = ExternalPillars.query.filter(
            ExternalPillars.date >= session["start_date"],
            ExternalPillars.date <= session["end_date"]
        ).count()

        window_size = math.ceil(num_days/ 25)

        dates = ExternalPillars.query.filter(
            ExternalPillars.date >= session["start_date"] - timedelta(days=window_size),
            ExternalPillars.date <= session["end_date"]
        ).all()

        chart = NatalChart.query.filter_by(id=session["contact_name_id"]).one()
        n_chart_stems = [chart.hour_s, chart.day_s, chart.month_s, chart.year_s] 
        n_chart_branches = [chart.hour_e, chart.day_e, chart.month_e, chart.year_e]
        data = calc_comb_clash(n_chart_stems, n_chart_branches, dates)

        comb_list = [e["e_combine"] for e in data]
        clash_list = [e["e_clash"] for e in data]

        avg_combine = [round(np.mean(comb_list), 2)] * len(data)
        avg_clash = [round(np.mean(comb_list), 2)] * len(data)

        rolling_data_comb = comb_list[:window_size - 1] + rolling_avg(comb_list, window_size)
        rolling_data_clash = comb_list[:window_size - 1] + rolling_avg(clash_list, window_size)

    return render_template('timeline.jinja2', 
        form=date_form,
        user_chart=chart,
        natal_chart=natal_chart_list,
        choice_form=choice_form,
        session=session,
        data=data[window_size:],
        labels=[d.date for d in dates[window_size:]],
        avg_combine=avg_combine,
        avg_clash=avg_clash,
        rolling_data=rolling_data_comb[window_size:],
        rolling_data_clash=rolling_data_clash[window_size:]
    )

def rolling_avg(data, window_size):
    numbers_series = pd.Series(data)
    windows = numbers_series.rolling(window_size)
    moving_averages = windows.mean()
    moving_averages_list = moving_averages.tolist()
    without_nans = moving_averages_list[window_size - 1:]
    return [round(w,2) for w in without_nans]
 