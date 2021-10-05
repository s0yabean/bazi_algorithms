from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import validators, SelectField, SubmitField, StringField, BooleanField
from datetime import datetime
from wtforms.fields.html5 import DateField

class ChartFormManual(FlaskForm):

    name = StringField('Name',validators=[DataRequired()])

    stem_choices = [("Jia",'Jia'),("Yi",'Yi'),("Bing",'Bing'),("Ding",'Ding'),("Wu",'Wu'),("Ji",'Ji'),("Gen",'Gen'),("Xin",'Xin'),('Ren','Ren'),("Gui",'Gui')]
    branch_choices = [("Zi",'Zi'),("Chou",'Chou'),("Yin",'Yin'),("Mao",'Mao'),("Chen",'Chen'),("Si",'Si'),("Wu",'Wu'),("Wei",'Wei'),("Shen",'Shen'),("You",'You'),("Xu",'Xu'),("Hai",'Hai')]
    hour_stem = SelectField('Hour Stem', choices=[(None, "")] + stem_choices)
    hour_branch = SelectField('Hour Branch', choices=[(None, "")] + branch_choices)
    day_stem = SelectField('Day Stem', [DataRequired()], choices=stem_choices)
    day_branch = SelectField('Day Branch', [DataRequired()], choices=branch_choices)
    month_stem = SelectField('Month Stem', [DataRequired()], choices=stem_choices)
    month_branch = SelectField('Month Branch', [DataRequired()], choices=branch_choices)
    year_stem = SelectField('Year Stem', [DataRequired()], choices=stem_choices)
    year_branch = SelectField('Year Branch', [DataRequired()], choices=branch_choices)
    my_own_chart_checkbox = BooleanField('(This is My Own Chart)')
    submit = SubmitField('Submit')

class ChartFormBirthTime(FlaskForm):

    name = StringField('Name',validators=[DataRequired()])
    birth_date = DateField('Birthday', format='%Y-%m-%d', default=datetime(1985, 1, 30), validators=(DataRequired(),))
    hour_choices = [("12am-1am",'12am-1am'),("1am-3am",'1am-3am'),("3am-5am",'3am-5am'),("5am-7am",'5am-7am'),("7am-9am",'7am-9am'),("9am-11am",'9am-11am'),("11am-1pm",'11am-1pm'),("1pm-3pm",'1pm-3pm'),('3pm-5pm','3pm-5pm'),("5pm-7pm",'5pm-7pm'),("7pm-9pm",'7pm-9pm'),("9pm-11pm",'9pm-11pm'),("11pm-12pm",'11pm-12pm')]
    hour_range = SelectField('Hour Range', choices=[(None, "")] + hour_choices)
    gender = SelectField('Gender', choices=[("False", "Female"), ("True", "Male")], validators=(DataRequired(),))
    my_own_chart_checkbox = BooleanField('(This is My Own Chart)')
    submit = SubmitField('Submit')

