from model import User, Project, Task, connect_to_db
from flask_login import current_user


"""User related functions"""
def create_user(username, password):
    user = User(
        username = username,
        password=password
    )
    return user

def get_users():
    return User.Query.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_user_by_username(username):
    return User.query.get(username)

def get_user_by_login(username, password):
    return User.query.filter_by(username=username, password=password).first()

""" Project related functions"""
def create_project(project_name, project_description, user_id):
    project = Project(
        project_name = project_name,
        project_description = project_description,
        user_id= user_id
    )
    return project

def get_projets():
    return Project.query.all()

def get_project_by_id(project_id):
    return Project.query.get(project_id)

def get_project_by_name(name):
    return Project.query.get(name)

def current_user_projects(id):
    return Project.query.filter(Project.user_id == id)
    

"""Task related function"""
def create_task(task_name, task_description, status, project_id):
   task = Task(
       task_name = task_name,
       task_description = task_description,
       status = status,
       project_id = project_id
   ) 
   return task

def get_tasks():
    return Task.query.all()

def get_task_by_id(task_id):
    return Task.query.get(task_id)

def get_task_by_name(name):
    return Task.query.get(name)
