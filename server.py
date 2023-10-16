from flask import Flask, render_template
from model import connect_to_db

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "main":
    connect_to_db(app)
    app.run(debug=True)