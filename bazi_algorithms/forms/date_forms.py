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

    def validate_on_submit(self):
        print(self.startdate.data)
        print(self.enddate.data)

        if self.enddate.data is not None:
            if (self.startdate.data > self.enddate.data):
                flash(f"End Date ({self.enddate.data}) cannot be before Start Date ({self.startdate.data})",  'error')
                return False
            return True

class TimelineDateForm(FlaskForm):
    default_start = datetime(int(str(datetime.today())[:4]), 1, 1)
    startdate = DateField('Start Date', format='%Y-%m-%d', default=default_start, validators=(DataRequired(),))
    enddate = DateField('End Date', format='%Y-%m-%d', default=datetime(int(str(datetime.today())[:4]), 12, 31), validators=(DataRequired(),))
    submit = SubmitField('Submit')