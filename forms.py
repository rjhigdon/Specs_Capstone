from flask_wtf import FlaskForm
from flask import flash
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, InputRequired, ValidationError
from model import User, Project, Task

class RegisterForm(FlaskForm):
    username = StringField("Username:", validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired()])
    submit = SubmitField("Submit")

    def user_validate(self, username):
        existing_username_query = User.query.filter_by(username = username.data).first()
        
        if existing_username_query:
            raise ValidationError("That username already exists. Try again")
                    
class LoginForm(FlaskForm):
    username = StringField("Username:", validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired()])
    submit = SubmitField("Submit")
    

class ProjectForm(FlaskForm):
    project_name = StringField("Name:", validators=[DataRequired()])
    project_description = StringField("Description:")
    submit=SubmitField("Submit")
    
    def project_validate(self, project_name):
        project_checker = Project.query.filter_by(project_name = project_name.data).first()
        
        if project_checker:
            raise ValidationError(
                "This project name already exists. Use another"
            )

class TaskForm(FlaskForm):
    task_name = StringField("Name:")
    task_description = StringField("description")
    status = SelectField("status", choices=[('Backlog', 'Backlog'), ('To-Do', 'To-Do'), ('In-Progress', 'In-Progress'), ('Completed', 'Completed')])
    submit=SubmitField("Submit")
    