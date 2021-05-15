from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import validators, SelectField

class ChoiceForm(FlaskForm):
     contact_name = SelectField([DataRequired()])

class NetworkForm(FlaskForm):
     question = SelectField([DataRequired()])