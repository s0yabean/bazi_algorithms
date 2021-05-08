"""Forms to submit text for AI Model"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError
from flask import session, flash

class AiForm(FlaskForm):
    """Submit user input"""
    input_text = TextAreaField(
        'Input Text',
        validators=[
            DataRequired(),
            Length(min=15, message='Text has to be longer.')
        ]
    )
    submit = SubmitField('Submit')

class SaveProfileForm(FlaskForm):
    """Save Profile of User"""
    input_name = StringField(
        'Profile Name',
        validators=[
            DataRequired(),
            Length(min=2, message='Name has to be longer.')
        ]
    )
    submit_field = SubmitField('Save Profile')

    def validate_input_name(self, input_name):
        print(f"session: {session}")
        count = len(session["input_text"])
        print(f"count: {count}")
        if count == 0:
            flash("No data entered yet, cannot create Profile.",  'error')
            raise ValidationError()
