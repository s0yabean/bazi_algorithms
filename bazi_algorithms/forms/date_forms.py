from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from wtforms import validators, SubmitField

class DateForm(FlaskForm):
    startdate = DateField('Start Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    enddate = DateField('End Date', format='%Y-%m-%d', validators=(validators.DataRequired(),))
    submit = SubmitField('Submit')