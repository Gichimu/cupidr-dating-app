from flask_wtf import FlaskForm
from wtforms import TextAreaField, TextField, IntegerField, SelectField, SubmitField, validators
from wtforms.validators import Required

class updateForm(FlaskForm):
    age = IntegerField('Your age', validators=[Required()])
    gender = SelectField('Sex', ['Male', 'Female'])
    complexion = SelectField('Complexion', ['Light-skinned', 'Medium', 'Dark-skinned'])
    personality = SelectField('Personality type', ['Outgoing', ''])

