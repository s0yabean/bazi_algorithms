from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import validators, SelectField, SubmitField

class ChartForm(FlaskForm):
    stem_choices = [(1,'Jia'),(2,'Yi'),(3,'Bing'),(4,'Ding'),(5,'Wu'),(6,'Ji'),(7,'Gen'),(8,'Xin'),(9,'Ren'),(10,'Gui')]
    branch_choices = [(1,'Zi'),(2,'Chou'),(3,'Yin'),(4,'Mao'),(5,'Chen'),(6,'Si'),(7,'Wu'),(8,'Wei'),(9,'Shen'),(10,'You'),(11,'Xu'),(12,'Hai')]
    hour_stem = SelectField('Hour Stem', choices=[(None, "")] + stem_choices)
    hour_branch = SelectField('Hour Branch', choices=[(None, "")] + branch_choices)
    day_stem = SelectField('Day Stem', [DataRequired()], choices=stem_choices)
    day_branch = SelectField('Day Branch', [DataRequired()], choices=branch_choices)
    month_stem = SelectField('Month Stem', [DataRequired()], choices=stem_choices)
    month_branch = SelectField('Month Branch', [DataRequired()], choices=branch_choices)
    year_stem = SelectField('Year Stem', [DataRequired()], choices=stem_choices)
    year_branch = SelectField('Year Branch', [DataRequired()], choices=branch_choices)
    submit = SubmitField('Submit')
