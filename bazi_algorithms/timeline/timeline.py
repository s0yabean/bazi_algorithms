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
    from ..forms.name_forms import TestForm, ChoiceForm
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

    # df = pd.read_csv("/Users/tonytong/Desktop/bazi_2021_external_data.csv")
    # results = pd.read_csv("/Users/tonytong/Desktop/bazi_2021_my_chart_results.csv")
    # if 'startdate' in session.keys():
    #     df = df[(df["date"] >= str(session['startdate'])) & (df["date"] <= str(session['enddate']))]
    #e_combine = list(results["e_combine"])
    #e_clash = list(results["e_clash"])

    return render_template('timeline.jinja2', form=Dateform,
    natal_chart=natal_chart, choice_form=ChoiceForm,
    session=session)