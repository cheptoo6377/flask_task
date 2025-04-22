from flask import render_template
from app import app
from app.models import User




@app.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users=users, title = 'Home')

@app.route('/task')
def tasks():
    users = User.query.all()
    return render_template('task.html', title = 'Task', users=users)

@app.route('/user')
def user():
    users = User.query.all()
    return render_template('user.html',users=users, title = 'Users')