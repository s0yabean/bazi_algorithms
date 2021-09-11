from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import validators, SelectField, SubmitField, StringField

class ChartForm(FlaskForm):

    name = StringField('Name',validators=[DataRequired()])

    stem_choices = [("Jia",'Jia'),("Yi",'Yi'),("Bing",'Bing'),("Ding",'Ding'),("Wu",'Wu'),("Ji",'Ji'),("Gen",'Gen'),("Xin",'Xin'),('Ren','Ren'),("Gui",'Gui')]
    branch_choices = [("Zi",'Zi'),("Chou",'Chou'),("Yin",'Yin'),("Mao",'Mao'),("Chen",'Chen'),("Si",'Si'),("Wu",'Wu'),("Wei",'Wei'),("Shen",'Shen'),("You",'You'),("Hai",'Hai')]
    hour_stem = SelectField('Hour Stem', choices=[(None, "")] + stem_choices)
    hour_branch = SelectField('Hour Branch', choices=[(None, "")] + branch_choices)
    day_stem = SelectField('Day Stem', [DataRequired()], choices=stem_choices)
    day_branch = SelectField('Day Branch', [DataRequired()], choices=branch_choices)
    month_stem = SelectField('Month Stem', [DataRequired()], choices=stem_choices)
    month_branch = SelectField('Month Branch', [DataRequired()], choices=branch_choices)
    year_stem = SelectField('Year Stem', [DataRequired()], choices=stem_choices)
    year_branch = SelectField('Year Branch', [DataRequired()], choices=branch_choices)
    submit = SubmitField('Submit')
