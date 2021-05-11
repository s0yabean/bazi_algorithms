from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from wtforms import validators, SelectField
from datetime import datetime

class TestForm(FlaskForm):
     single_dynamic_select = SelectField(u"Hour", [DataRequired()],
            choices=[('1', '8am'), ('2', '10am') ],
            description=u"动态加载选项。",
            render_kw={})
     # hour = SelectField(u'Hour', choices=[('1', '8am'), ('2', '10am') ])

class ChoiceForm(FlaskForm):
     contact_name = SelectField([DataRequired()])