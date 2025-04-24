from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField ,BooleanField,SubmitField,PasswordField
from wtforms.validators import DataRequired


class Taskform(FlaskForm):
    title = StringField('Task Title', validators=[DataRequired()])
    description = TextAreaField( 'task description',  validators=[DataRequired()])
    completed = BooleanField('completed', default=False)
    submit = SubmitField('Submit')

class Userform(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    firstname = StringField('First Name',  validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('register')
    