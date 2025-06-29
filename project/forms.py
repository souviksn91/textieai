# project/forms.py
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length

def validate_word_count(form, field):
    word_count = len(field.data.split())
    if word_count > 30:
        raise ValidationError(f"Text must be 30 words or less (Current: {word_count} words)")

class TextCorrectionForm(FlaskForm):
    text = TextAreaField('Your Text', validators=[DataRequired(), validate_word_count])
    submit = SubmitField('Correct Grammar')


