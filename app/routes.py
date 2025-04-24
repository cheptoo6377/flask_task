from flask import render_template,redirect,url_for,flash
from app import app,db
from app.models import User,Task
from app.forms import Taskform
from app.forms import Userform





@app.route('/')
def home():
    users = User.query.all()
    tasks = Task.query.all()
    return render_template('index.html', users=users, tasks=tasks, title = 'Home')

@app.route('/task',methods=['GET', 'POST'])
def tasks():
    form = Taskform()

    if form.validate_on_submit():
        new_task = Task(title=form.title.data,description=form.description.data,completed=form.completed.data,user_id= 1)
        
        db.session.add(new_task)
        db.session.commit()
        flash(f'Task {new_task.title} created successfully','success')
        return redirect(url_for("home"))
    return render_template('task.html', title = 'Task',  form=form,users=User.query.all())

@app.route('/register',methods=['GET', 'POST'])
def register():
    form = Userform()
    if form.validate_on_submit():
        new_user = User(username=form.username.data,firstname=form.firstname.data,lastname=form.lastname.data,password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash(f'registration for {new_user.firstname} successful','success')
        return redirect(url_for("home"))

    return render_template('register.html', title = 'Register',form=form)

@app.route('/toggle_task/<int:task_id>',methods=['POST'])
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    flash(f'Task {task.title} status updated to ', 'success')
    return redirect(url_for('home'))
    
    
@app.route('/delete_task/<int:task_id>',methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash(f'Task {task.title} deleted successfully', 'success')
    return redirect(url_for('home'))
@app.route('/delete_user/<int:user_id>',methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash(f'User {user.username} deleted successfully', 'success')
    return redirect(url_for('home'))