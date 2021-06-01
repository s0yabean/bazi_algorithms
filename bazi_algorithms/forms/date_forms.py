from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms import SubmitField
from datetime import datetime
from flask import session, flash
from wtforms.validators import DataRequired, ValidationError

class DateForm(FlaskForm):
    startdate = DateField('Start Date', format='%Y-%m-%d', default=datetime.today, validators=(DataRequired(),))
    enddate = DateField('End Date', format='%Y-%m-%d', validators=(DataRequired(),))
    submit = SubmitField('Submit')

    # def validate_on_submit(self):
    #     if self.enddate.data is not None:
    #         if (self.startdate.data > self.enddate.data):
    #             flash(f"End Date ({self.enddate.data}) cannot be before Start Date ({self.startdate.data})",  'error')
    #             return False
    #         return True