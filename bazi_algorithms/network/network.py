from re import I, L
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
    from ..forms.network_forms import NetworkForm_2
    from ..persistence.models import NatalChart, ExternalPillars
    from .explanations import explanation_list_paid, explanation_list_free

    table_data = NatalChart.query.filter_by(user_id=current_user.id, self_chart=False).all() 
    natal_chart_id = current_user.natal_chart_id
    remarks = []
    explanations = None
    show_success_flash = False 
    questions = question_list()
    user_chart = None
    NetworkForm_2 = NetworkForm_2()

    if request.method == 'GET':
        if current_user.natal_chart_id is None:
            flash("Please add in your own chart in the Account section for some questions to work.", "info")
            return render_template(
                'network.jinja2',
                current_user=current_user,
                table_data = table_data,
                network_form_2=NetworkForm_2,
                questions=[],
                remarks=[],
                explanations=[],
                user_chart=user_chart)

    if NetworkForm_2.validate_on_submit():
        if NetworkForm_2.startdate.data is not None and NetworkForm_2.enddate.data is not None:
            days_apart = (NetworkForm_2.enddate.data - NetworkForm_2.startdate.data).days
            if days_apart <= 1:
                flash(f"Date Range of {NetworkForm_2.startdate.data} to {NetworkForm_2.enddate.data} Needs To Be At Least 2 Days Apart. Current range: {days_apart} day.",  'error')
                return render_template(
                'network.jinja2',
                current_user=current_user,
                table_data = table_data,
                network_form_2=NetworkForm_2,
                questions=[],
                remarks=[],
                explanations=[],
                user_chart=user_chart)

        show_success_flash = True
        if NetworkForm_2.category.data is not None:
            session['question'] = int(NetworkForm_2.category.data)
        
        session['start_date'] = NetworkForm_2.startdate.data
        session['end_date'] = NetworkForm_2.enddate.data

    if 'question' in session.keys():
        if session['question'] in [1,2,3,4]:
            if ('start_date' not in session.keys() and 'end_date' not in session.keys()) or (session['start_date'] is None or session['end_date'] is None):
                flash("Please Select A Date Range", "error")
                table_data, remarks = [], []
            elif (session['start_date'] > session['end_date']):
                flash(f"End Date ({session['end_date']}) cannot be before Start Date ({session['start_date']}). Please change date range.", "error")
                table_data, remarks = [], []
            else:
                table_data, remarks = answer_question(questions[session['question']], table_data, natal_chart_id, session['start_date'], session['end_date'])
                
                if show_success_flash:
                    flash("Calculation Success.","info")
        elif session['question'] in [0,5,6,7]:
            if current_user.natal_chart_id is None:
                flash("Please add in your own chart in the Account section for some questions to work.", "info")
                flash("Personal chart not found, unable to answer question.", "error")
                return render_template(
                'network.jinja2',
                current_user=current_user,
                table_data = table_data,
                network_form_2=NetworkForm_2,
                questions=[],
                remarks=[],
                explanations=[],
                user_chart=user_chart)

            table_data, remarks = answer_question(questions[session['question']], table_data, natal_chart_id, "", "")
            if show_success_flash:
                flash("Calculation Success.","info")

        if current_user.plan == "Lite Plan":
            explanations = explanation_list_free()
        else:
            explanations = explanation_list_paid()

        for i in range(len(explanations)):
            if questions[session['question']] == explanations[i][0][1]:
                explanations = explanations[i]
                break

        if NatalChart.query.filter_by(id=current_user.natal_chart_id).all() != []:
            user_chart = NatalChart.query.filter_by(id=current_user.natal_chart_id).one()

            
    return render_template(
        'network.jinja2',
        current_user=current_user,
        table_data = table_data,
        network_form_2=NetworkForm_2,
        questions=questions,
        remarks=remarks,
        explanations=explanations,
        user_chart=user_chart)

from ..bazi_formulas.combines import count_earth_combo, count_earth_six_harmony_combine
from ..persistence.models import NatalChart, ExternalPillars
from .questions_1 import career_plus
from .questions_6_7 import nobleman_star, peach_blossom_me_to_others, peach_blossom_others_to_me
from .questions_2_3_4_5 import easiest_sell, more_prod, more_reckless, more_rebellious
def answer_question(input, table_data, natal_chart_id, start_date, end_date):
    ques = question_list()
    if input == ques[0]:
        return career_plus(table_data, natal_chart_id)
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

def question_list():
    return ["Who would be a good career partner/ colleague/ mentor?", 
                 "Who is easiest to sell to this period?",
                 "Who is more hardworking/ productive than normal this period?",
                 "Who is more reckless than normal this period?",
                 "Who is more rebellious than normal this period?",
                 "Who are my nobleman (贵人)?",
                 "Who am I more attracted to (has my peach blossom)?",
                 "Who is attracted to me (I have their peach blossom)?"]
