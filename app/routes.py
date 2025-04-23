from flask import render_template
from app import app
from app.models import User
from app.forms import Taskform
from app.forms import Userform




@app.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users=users, title = 'Home')

@app.route('/task',methods=['GET', 'POST'])
def tasks():
    form = Taskform()
    return render_template('task.html', title = 'Task',  form=form)

@app.route('/user',methods=['GET', 'POST'])
def user():
    form = Userform()
    users = User.query.all()
    return render_template('user.html',users=users, title = 'Users',form=form)