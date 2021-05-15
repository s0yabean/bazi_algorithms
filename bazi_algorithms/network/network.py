from re import L
from bazi_algorithms.persistence.models import NatalChart
from flask import Blueprint, redirect, render_template, url_for, flash, session, request, abort
from flask_login import current_user, login_required
from flask_wtf.csrf import CSRFProtect
import pandas as pd
from datetime import date
import numpy as np
from .. import db

network_bp = Blueprint(
    'network_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@network_bp.route("/network", methods=['GET', 'POST'])
@login_required
def main():
    from ..forms.date_forms import DateForm
    from ..forms.name_forms import NetworkForm
    from ..persistence.models import NatalChart, ExternalPillars
    """Table showing natal charts belonging to my account."""
    table_data = NatalChart.query.filter_by(user_id=current_user.id).all() 
    natal_chart_id = current_user.natal_chart_id
    remarks = []

    Dateform = DateForm()
    if Dateform.validate_on_submit():
        session['start_date'] = Dateform.startdate.data
        session['end_date'] = Dateform.enddate.data
        return redirect(url_for('network_bp.main'))

    if request.method == 'POST':
        if "dropdown_menu" and "security_key" in request.form.keys():
            session['question'] = request.form["dropdown_menu"] 
            
    NetworkForm = NetworkForm()
    questions = question_list()

    if 'question' in session.keys():
        if session['question'] in questions[:5]:
            if 'start_date' not in session.keys() and 'end_date' not in session.keys():
                flash("Please select a date range", "info")
            else:
                table_data, remarks = answer_question(session['question'], table_data, natal_chart_id, session['start_date'], session['end_date'])
        elif session['question'] in questions[5:]:
            table_data, remarks = answer_question(session['question'], table_data, natal_chart_id, "", "")

    return render_template(
        'network.jinja2',
        current_user=current_user,
        table_data = table_data,
        form=Dateform,
        network_form=NetworkForm,
        questions=questions,
        remarks=remarks)

from ..bazi_formulas.combines import count_earth_combo, count_earth_six_harmony_combine
from ..persistence.models import NatalChart, ExternalPillars
from .questions_1 import career_plus
from .questions_6_7 import nobleman_star, peach_blossom_me_to_others, peach_blossom_others_to_me
from .questions_2_3_4_5 import easiest_sell, more_prod, more_reckless, more_rebellious
def answer_question(input, table_data, natal_chart_id, start_date, end_date):
    ques = question_list()
    if input == ques[0]:
        return career_plus(table_data, start_date, end_date)
    elif input == ques[1]:
        return easiest_sell(table_data, start_date, end_date)
    elif input == ques[2]:
        return more_prod(table_data, start_date, end_date)
    elif input == ques[3]:
        return more_reckless(table_data, start_date, end_date)
    elif input == ques[4]:
        return more_rebellious(table_data, start_date, end_date)
    elif input == ques[5]:
        return nobleman_star(table_data, natal_chart_id)
    elif input == ques[6]:
        return peach_blossom_me_to_others(table_data, natal_chart_id)
    elif input == ques[7]:
        return peach_blossom_others_to_me(table_data, natal_chart_id)
    # elif input == ques[7]:
    #     return attracts_me(table_data, natal_chart_id, start_date, end_date)
    # elif input == ques[8]:
    #     return attracts_me(table_data, natal_chart_id, start_date, end_date)

def question_list():
    return ["Who would be a good career partner/ colleague/ mentor?", 
                 "Who is easiest to sell to this period?",
                 "Who is more hardworking/ productive than normal this period?",
                 "Who is more reckless than normal this period?",
                 "Who is more rebellious than normal this period?",
                 "Who are my nobleman (贵人)?",
                 "Who am I more attracted to (has my peach blossom)?",
                 "Who is attracted to me (I have their peach blossom)?",
                 "Who is open to romantic relationships?"]