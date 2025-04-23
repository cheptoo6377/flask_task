from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField ,BooleanField,SubmitField,PasswordField


class Taskform(FlaskForm):
    title = StringField('Task Title')
    description = TextAreaField( 'task description')
    completed = BooleanField('completed')
    submit = SubmitField('Submit')

class Userform(FlaskForm):
    username = StringField('Username')
    firstname = StringField('First Name')
    lastname = StringField('Last Name')
    password = PasswordField('Password')
    submit = SubmitField('Submit')
    