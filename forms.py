from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
from model import User

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=25)] )
    password = PasswordField("Password", validators=[DataRequired(), Length(min=4, max=25)])
    submit = SubmitField("Submit")

    def user_validate(self, username):
        username_checker = User.query.filter_by(username = username.data).first()
        
        if username_checker:
            raise ValidationError(
                "That username already exists. Try again"
            )
            
class LoginForm(FlaskForm):
    username = StringField("Username:", validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField("Password:", validators=[DataRequired(), Length(min=4, max=25)])
    submit = SubmitField("Submit")

    def user_validate(self, username):
        username_checker = User.query.filter_by(username = username.data).first()
        
        if username_checker:
            raise ValidationError(
                "That username already exists. Try again"
            )

class ProjectForm(FlaskForm):
    pass

class TaskForm(FlaskForm):
    pass