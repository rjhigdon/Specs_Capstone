from forms import RegisterForm, LoginForm, ProjectForm
import crud
from model import db, User, Project, Task, connect_to_db

from flask import (Flask, render_template, flash, redirect, url_for, session, request)
from flask_login import LoginManager, login_user
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "supa dupa secret"
app.jinja_env.undefined = StrictUndefined

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id);

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user)
        return redirect(url_for("projects"))
           
    return render_template("login.html", form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
    
    return render_template("register.html", form=form)
    

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)