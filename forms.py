from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
from model import User, Project, Task

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

    def user_validate(self, username):
        username_checker = User.query.filter_by(username = username.data).first()
        
        if username_checker:
            raise ValidationError(
                "That username already exists. Try again"
            )
            
class LoginForm(FlaskForm):
    username = StringField("Username:", validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired()])
    submit = SubmitField("Submit")

    def user_validate(self, username):
        username_checker = User.query.filter_by(username = username.data).first()
        
        if username_checker:
            raise ValidationError(
                "That username already exists. Try again"
            )

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
    description = StringField("description")
    status = SelectField("status", choices=[('Backlog', 'Backlog'), ('To-Do', 'To-Do'), ('In-Progress', 'In-Progress'), ('Done', 'Done')])
    