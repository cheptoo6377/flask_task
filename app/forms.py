from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField ,BooleanField,SubmitField,PasswordField
from wtforms.validators import DataRequired


class Taskform(FlaskForm):
    title = StringField('Task Title')
    description = TextAreaField( 'task description')
    completed = BooleanField('completed')
    submit = SubmitField('Submit')

class Userform(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    firstname = StringField('First Name',  validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('register')
    