from flask import render_template,redirect,url_for
from app import app,db
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

@app.route('/register',methods=['GET', 'POST'])
def register():
    form = Userform()
    if form.validate_on_submit():
        new_user = User(username=form.username.data,firstname=form.firstname.data,lastname=form.lastname.data,password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template('register.html', title = 'Register',form=form)
