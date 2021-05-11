from flask import Blueprint, redirect, render_template, url_for, flash, session, request, abort
from flask_login import current_user, login_required
from flask_wtf.csrf import CSRFProtect
import pandas as pd

timeline_bp = Blueprint(
    'timeline_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@timeline_bp.route("/timeline", methods=['GET', 'POST'])
@login_required
def main():
    from ..forms.date_forms import DateForm
    from ..forms.name_forms import ChoiceForm
    from ..persistence.models import User, NatalChart, ExternalPillars

    natal_chart = NatalChart.query.filter_by(user_id=current_user.id).all()
    ChoiceForm = ChoiceForm()
    if request.method == 'POST':
        print(request.form)
        if "dropdown_menu" and "security_token" in request.form.keys():
            contact_id = request.form["dropdown_menu"]
            contact_name = NatalChart.query.filter_by(id=contact_id).one().contact_name
            session['contact_name_id'] = contact_id 
            session['contact_name'] = contact_name
            # calculate data and pass to chart
            pass

    Dateform = DateForm()
    if Dateform.validate_on_submit():
        session['start_date'] = Dateform.startdate.data
        session['end_date'] = Dateform.enddate.data
        return redirect(url_for('timeline_bp.main'))

    if 'start_date' and 'end_date' and 'contact_name_id' and 'contact_name' in session.keys():
        dates = ExternalPillars.query.filter(ExternalPillars.date >= session["start_date"], ExternalPillars.date <= session["end_date"]).all()
        chart = NatalChart.query.filter_by(id=session["contact_name_id"]).one()
        n_chart_stems = [chart.hour_s, chart.day_s, chart.month_s, chart.year_s] 
        n_chart_branches = [chart.hour_e, chart.day_e, chart.month_e, chart.year_e]
        data = calc_comb_clash(n_chart_stems, n_chart_branches, dates)
        print(data)

        #df = pd.read_csv("/Users/tonytong/Desktop/bazi_2021_external_data.csv")
    # results = pd.read_csv("/Users/tonytong/Desktop/bazi_2021_my_chart_results.csv")
    # if 'startdate' in session.keys():
    #     df = df[(df["date"] >= str(session['startdate'])) & (df["date"] <= str(session['enddate']))]
    #e_combine = list(results["e_combine"])
    #e_clash = list(results["e_clash"])

    return render_template('timeline.jinja2', form=Dateform,
    natal_chart=natal_chart, choice_form=ChoiceForm,
    session=session, data=data, labels=[d.date for d in dates])

 
from ..bazi_formulas.combines import count_earth_combo, count_earth_six_harmony_combine, count_stem_combine, earth_full_combo_finder, earth_two_third_combo_finder
from ..bazi_formulas.clashes import count_stem_clash, count_earth_clash
def calc_comb_clash(natal_stem, natal_earth, dates):
    result = []
    for i in range(len(dates)):
        external_stem = []
        external_earth = []
        li = [dates[i].day_pillar, dates[i].month_pillar, dates[i].year_pillar]
        for item in li:
            s = item.split(' ')
            external_stem.append(s[0])
            external_earth.append(s[1])
     
        e_harmony_combine = count_earth_six_harmony_combine(natal_earth, external_earth)
        e_combo_combine = count_earth_combo(natal_earth, external_earth)
        s_combine = count_stem_combine(natal_stem, external_stem)
        e_clash = count_earth_clash(natal_earth, external_earth)
        s_clash = count_stem_clash(natal_stem, external_stem)

        print([(s_combine, s_clash), (e_combo_combine + e_harmony_combine, e_clash)])
        row = {"s_combine":s_combine, "s_clash":s_clash, "e_combine":e_combo_combine + e_harmony_combine, "e_clash": e_clash}
        result.append(row)
    return result