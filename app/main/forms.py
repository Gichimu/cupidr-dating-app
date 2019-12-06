from flask_wtf import FlaskForm
from wtforms import TextAreaField, TextField, IntegerField, SelectField, SubmitField, validators
from wtforms.validators import Required

class updateForm(FlaskForm):
    age = IntegerField('Your age', validators=[Required()])
    gender = SelectField('Sex', choices=[('Male', 'Male'), ('Female', 'Female')])
    complexion = SelectField('Complexion', choices=[('Light-skinned', 'Light-skinned'), ('Medium', 'Medium'), ('Dark-skinned', 'Dark-skinned')])
    personality = SelectField('Personality type', choices=[('Outgoing', 'Outgoing'), ('introverted', 'introverted')])
    height = SelectField('Height', choices=[('short', 'Short'), ('medium', 'Medium'), ('tall', 'Tall')])
    submit = SubmitField('Submit')

class findMatches(FlaskForm):
    age = IntegerField('Age', validators=[Required()])
    gender = SelectField('Sex', choices=[('Male', 'Male'), ('Female', 'Female')])
    complexion = SelectField('Complexion', choices=[('Light-skinned', 'Light-skinned'), ('Medium', 'Medium'), ('Dark-skinned', 'Dark-skinned')])
    personality = SelectField('Personality type', choices=[('Outgoing', 'Outgoing'), ('introverted', 'introverted')])
    height = SelectField('Height', choices=[('short', 'Short'), ('medium', 'Medium'), ('tall', 'Tall')])
    submit = SubmitField('Submit')


