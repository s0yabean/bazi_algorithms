from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import Optional


class NetworkForm_2(FlaskForm):
    choices = [
        ("0", "Who would be a good career partner/ colleague/ mentor?"),
        ("1", "Who is easiest to sell to this period?"),
        ("2", "Who is more hardworking/ productive than normal this period?"),
        ("3", "Who is more reckless than normal this period?"),
        ("4", "Who is more rebellious than normal this period?"),
        ("5", "Who are my nobleman (贵人)?"),
        ("6", "Who am I more attracted to (has my peach blossom)?"),
        ("7", "Who is attracted to me (I have their peach blossom)?")
    ]
    category = SelectField('Category', choices=choices)
    startdate = DateField('Start Date', format='%Y-%m-%d', default=datetime.today, validators=[Optional()])
    enddate = DateField('End Date', format='%Y-%m-%d', validators=[Optional()])
    submit = SubmitField('Submit')
