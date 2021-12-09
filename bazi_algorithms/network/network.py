from bazi_algorithms.persistence.models import NatalChart
from flask import (
    Blueprint,
    render_template,
    flash,
    session,
    request
)
from flask_login import current_user, login_required

from ..forms.network_forms import NetworkForm_2
from ..persistence.models import NatalChart
from .explanations import explanation_list_paid, explanation_list_free

from .questions_1 import career_plus
from .questions_6_7 import nobleman_star, peach_blossom_me_to_others, peach_blossom_others_to_me
from .questions_2_3_4_5 import easiest_sell, more_prod, more_reckless, more_rebellious

network_bp = Blueprint(
    'network_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@network_bp.route("/network", methods=['GET', 'POST'])
@login_required
def main():
    table_data = NatalChart.query.filter_by(user_id=current_user.id, self_chart=False).all() 
    natal_chart_id = current_user.natal_chart_id
    remarks = []
    explanations = None
    show_success_flash = False 
    questions = question_list()
    user_chart = None
    total_other_ppl_charts =  0
    netform_2 = NetworkForm_2()

    if request.method == 'GET':
        if current_user.natal_chart_id is None:
            flash("Please add in your own chart in the Account section for some questions to work.", "info")
            return render_template(
                'network.jinja2',
                current_user=current_user,
                table_data = table_data,
                network_form_2=netform_2,

                questions=[], remarks=[], explanations=[],

                user_chart=user_chart,
                total_other_ppl_charts = total_other_ppl_charts
            )

    if netform_2.validate_on_submit():
        if netform_2.startdate.data is not None and netform_2.enddate.data is not None:
            days_apart = (netform_2.enddate.data - netform_2.startdate.data).days
            if days_apart <= 1:
                
                flash(f"Date Range of {netform_2.startdate.data} to {netform_2.enddate.data} Needs To Be At Least 2 Days Apart. "
                       "Current range: {days_apart} day.",  'error')

                return render_template(
                    'network.jinja2',

                    current_user=current_user,
                    table_data=table_data,
                    network_form_2=netform_2,

                    questions=[], remarks=[], explanations=[],

                    user_chart=user_chart,
                    total_other_ppl_charts=total_other_ppl_charts
                )

        show_success_flash = True
        if netform_2.category.data is not None:
            session['question'] = int(netform_2.category.data)
        
        session['start_date'] = netform_2.startdate.data
        session['end_date'] = netform_2.enddate.data

    sess_question = session.get('question')

    if sess_question is not None:
        if sess_question in [1,2,3,4]:

            sess_start_date = session.get('start_date', None)
            sess_end_date = session.get('end_date', None)

            remarks = []

            if not sess_start_date or not sess_end_date:
                flash("Please Select A Date Range", "error")
                table_data= []
            elif sess_start_date > sess_end_date:
                flash(f"End Date ({sess_end_date}) cannot be before Start Date ({sess_start_date}). "
                       "Please change date range.", "error")
                table_data = []
            else:
                table_data, remarks = answer_question(
                    questions[sess_question], 
                    table_data, 
                    natal_chart_id, 
                    sess_start_date, 
                    sess_end_date
                )
                
                if show_success_flash:
                    flash("Calculation Success.","info")


        elif sess_question in [0,5,6,7]:
            if current_user.natal_chart_id is None:
                flash("Please add in your own chart in the Account section for some questions to work.", "info")
                flash("Personal chart not found, unable to answer question.", "error")
                return render_template(
                    'network.jinja2',

                    current_user=current_user,
                    table_data = table_data,
                    network_form_2=netform_2,

                    questions=[], remarks=[], explanations=[],

                    user_chart=user_chart,
                    total_other_ppl_charts = total_other_ppl_charts
                )

            table_data, remarks = answer_question(questions[sess_question], table_data, natal_chart_id, "", "")

            if show_success_flash:
                flash("Calculation Success.","info")

        if current_user.plan == "Lite Plan":
            explanations = explanation_list_free()
        else:
            explanations = explanation_list_paid()

        for expl in explanations:
            if questions[sess_question] == expl[0][1]:
                explanations = expl
                break

        db_natal_chart = NatalChart.query.filter_by(id=current_user.natal_chart_id).first()

        if db_natal_chart is not None:
            user_chart = db_natal_chart
            total_other_ppl_charts = NatalChart.query.filter_by(user_id=current_user.id, self_chart=False).count()
            print("total_other_ppl_charts")
            print(total_other_ppl_charts)
            
    return render_template(
        'network.jinja2',

        current_user=current_user,
        table_data = table_data,
        network_form_2=netform_2,

        questions=questions,
        remarks=remarks,
        explanations=explanations,

        user_chart=user_chart,
        total_other_ppl_charts = total_other_ppl_charts
    )


def answer_question(qs_input, table_data, natal_chart_id, start_date, end_date):
    ques = question_list()
    if qs_input == ques[0]:
        return career_plus(table_data, natal_chart_id)
    elif qs_input == ques[1]:
        return easiest_sell(table_data, start_date, end_date)
    elif qs_input == ques[2]:
        return more_prod(table_data, start_date, end_date)
    elif qs_input == ques[3]:
        return more_reckless(table_data, start_date, end_date)
    elif qs_input == ques[4]:
        return more_rebellious(table_data, start_date, end_date)
    elif qs_input == ques[5]:
        return nobleman_star(table_data, natal_chart_id)
    elif qs_input == ques[6]:
        return peach_blossom_me_to_others(table_data, natal_chart_id)
    elif qs_input == ques[7]:
        return peach_blossom_others_to_me(table_data, natal_chart_id)

__all_questions = [
    "Who would be a good career partner/ colleague/ mentor?", 
    "Who is easiest to sell to this period?",
    "Who is more hardworking/ productive than normal this period?",
    "Who is more reckless than normal this period?",
    "Who is more rebellious than normal this period?",
    "Who are my nobleman (贵人)?",
    "Who am I more attracted to (has my peach blossom)?",
    "Who is attracted to me (I have their peach blossom)?"
]

def question_list():
    return __all_questions
