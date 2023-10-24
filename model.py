import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

""" Users Table """

class User(db.Model, UserMixin):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    
    projects = db.relationship("Project", backref="user", lazy=False)
    
    def to_json(self):        
        return {"username": self.username,
                "password": self.password}

    def is_authenticated(self):
        return True

    def is_active(self):   
        return True           

    def is_anonymous(self):
        return False          
    
    def get_id(self):
        return self.user_id
    
    def __repr__(self):
        return f"<User {self.user_id} exists with the username {self.username}>"

""" Projects Table """    
    
class Project(db.Model):
    
    __tablename__ = "projects"
    
    project_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_name = db.Column(db.String(40), nullable=False)
    project_description = db.Column(db.String(400))
    user_id = db.Column(db.Integer(), db.ForeignKey("users.user_id"), nullable =False)
    
    tasks = db.relationship("Task",  backref="project", lazy=False)
    
    def __repr__(self):
        return f"<Project:{self.project_id} is named: {self.project_name}>"
    
""" Tasks Table """
    
class Task(db.Model):
    
    __tablename__ = "tasks"

    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_name = db.Column(db.String(40), nullable=False)
    task_description = db.Column(db.String(400))
    status = db.Column(db.String)
    project_id= db.Column(db.Integer(), db.ForeignKey("projects.project_id"), nullable=False)    
    
    
    
    def __repr__(self):
        return f"<Task:{self.task_id} is named: {self.task_name} and has a status of {self.status}>"

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
    