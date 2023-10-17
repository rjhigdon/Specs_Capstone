import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

""" Users Table """

class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    
    projects = db.relationship("Project", backref="users")

    def __repr__(self):
        return f"<User {self.user_id} exists with the username {self.username}>"
    
class Project(db.Model):
    
    __tablename__ = "projects"
    project_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(400))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    
    tasks = db.relationship("Project", backref="projects", lazy= False)
    
    def __repr__(self):
        return f"<Project:{self.project_id} is named: {self.name}>"
    
class Task(db.Model):
    
    __tablename__ = "tasks"

    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(400))
    status = db.Column(db.String)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.project_id"))
    
    
    def __repr__(self):
        return f"<Task:{self.task_id} is named: {self.name} and has a status of {self.status}>"

def connect_to_db(flask_app, db_uri=os.environ["POSTGRES_URI"], echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)
    print("Connected to the db!")

if __name__ == "__main__":
    from server import app
    connect_to_db(app)
