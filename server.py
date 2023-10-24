from forms import RegisterForm, LoginForm, ProjectForm,TaskForm
from model import db, User, Project, Task, connect_to_db
from crud import current_user_projects

from flask import (Flask, render_template, flash, redirect)
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "supa dupa secret"
app.jinja_env.undefined = StrictUndefined


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        flash(f"User: {form.username.data} successfully registered")
        db.session.add(new_user)
        db.session.commit()
        return redirect("/login")
    else:
        flash("That username already exists. Try another")
    
    return render_template("register.html", form=form)
    
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print(form.username.data)
    print(form.validate_on_submit())
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(user)
        if user:
            if form.password.data == user.password:
                login_user(user)
                flash(f"Logged in as {user.username}")
                return redirect("/projects")
            else:
                flash("Username or Password was incorrect. Try again")
           
    return render_template("login.html", form=form)

@app.route("/projects", methods=["POST", "GET"])
@login_required
def all_projects():
    form = ProjectForm()
    if form.is_submitted():
        new_project = Project(
            project_name=form.project_name.data, 
            project_description=form.project_description.data, 
            user_id=current_user.user_id
            )
        db.session.add(new_project)
        db.session.commit()
        return redirect("/projects")
    
    user = current_user
    results = current_user_projects(user.user_id)
    return render_template("all_projects.html", user=user, results=results, form=form)

@app.route("/projects/<int:project_id>",methods=["GET", "POST"])
@login_required
def project(project_id):
    current_project = Project.query.get(project_id)
    form=TaskForm()
    if form.is_submitted():
        new_task = Task(
            task_name = form.task_name.data,
            task_description = form.task_description.data,
            status = form.status.data,
            project_id = current_project.project_id
            )
        db.session.add(new_task)
        db.session.commit()
        return redirect("/projects/{0}".format(project_id))
    
    current_project_tasks = current_project.tasks
    
    if current_project.tasks:
        tasks_for_backlog = current_project.tasks
        backlog_tasks = []
        for tasks in tasks_for_backlog:
            if tasks.status=="Backlog":
                backlog_tasks.append(tasks)

        tasks_for_todo = current_project.tasks
        todo_tasks = []
        for tasks in tasks_for_todo:
            if tasks.status=="To-Do":
                todo_tasks.append(tasks)

        tasks_for_in_progress = current_project.tasks
        in_progress_tasks = []
        for tasks in tasks_for_in_progress:
            if tasks.status=="In-Progress":
                in_progress_tasks.append(tasks)
        
        tasks_for_completed = current_project.tasks
        completed_tasks = []
        for tasks in tasks_for_completed:
            if tasks.status=="Completed":
                completed_tasks.append(tasks)
        
        return render_template("project.html", project=Project, tasks=tasks, backlog_tasks=backlog_tasks, todo_tasks=todo_tasks, in_progress_tasks=in_progress_tasks, completed_tasks=completed_tasks, current_project_tasks=current_project_tasks, form=form)
    
    else:
        return render_template("project.html", project=Project, current_project_tasks=current_project_tasks, form=form)

@app.route("/Backlog/<task_id>")  
def backlog_update(task_id):
    
    current_task = Task.query.filter(Task.task_id==task_id).first()
    current_task.status = "Backlog"
    db.session.commit()
    return redirect(f"/projects/{current_task.project_id}")

@app.route("/To-Do/<task_id>")  
def todo_update(task_id):
    
    current_task = Task.query.filter(Task.task_id==task_id).first()
    current_task.status = "To-Do"
    db.session.commit()
    return redirect(f"/projects/{current_task.project_id}")

@app.route("/In-Progress/<task_id>")  
def in_progress_update(task_id):
    current_task = Task.query.filter(Task.task_id==task_id).first()
    current_task.status = "In-Progress"
    db.session.commit()
    return redirect(f"/projects/{current_task.project_id}")

@app.route("/Completed/<task_id>")  
def completed_update(task_id):
    current_task = Task.query.filter(Task.task_id==task_id).first()
    print(current_task.status)
    current_task.status = "Completed"
    db.session.commit()
    print(current_task.status)
    return redirect(f"/projects/{current_task.project_id}")

@app.route("/delete/<task_id>")
def delete_task(task_id):
    current_task = Task.query.filter(Task.task_id==task_id).first()
    if current_task:
        db.session.delete(current_task)
        db.session.commit()
        return redirect(f"/projects/{current_task.project_id}")
    else:
        return redirect(f"/projects")

@app.route("/project_delete/<project_id>")
def delete_project(project_id):
    current_project = Project.query.filter(Project.project_id==project_id).first()
    current_tasks = Task.query.filter(Task.project_id == project_id).all()
    if current_tasks:
        for tasks in current_tasks:
            db.session.delete(tasks)
            db.session.delete(current_project)
            db.session.commit()
    else:
        db.session.delete(current_project)
        db.session.commit()
    return redirect("/projects")
    
    
@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect("/login")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)