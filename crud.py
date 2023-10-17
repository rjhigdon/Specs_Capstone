from model import User, Project, Task, connect_to_db


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


""" Project related functions"""
def create_project(name, description, status):
    project = Project(
        name = name,
        description = description,
        status = status,
    )
    return project

def get_projets():
    return Project.query.all()

def get_project_by_id(project_id):
    return Project.query.get(project_id)

def get_project_by_name(name):
    return Project.query.get(name)


"""Task related function"""
def create_task(name, description, status):
   task = Task(
       name = name,
       description = description,
       status = status
   ) 
   return task

def get_tasks():
    return Task.query.all()

def get_task_by_id(task_id):
    return Task.query.get(task_id)

def get_task_by_name(name):
    return Task.query.get(name)