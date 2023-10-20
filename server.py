
from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from model import db
from jinja2 import StrictUndefined
from forms import RegisterForm, LoginForm
# from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = "supa dupa secret"
app.jinja_env.undefined = StrictUndefined

# login_manager = LoginManager()
# login_manager.init_app(app)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", form=form)

@app.route("/register")
def register():
    form = RegisterForm()
    return render_template("register.html", form=form)
    

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)