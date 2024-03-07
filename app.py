from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    error = None
    return render_template('home.html', error=error)

@app.route("/<page>")
def page(page):
    return f"You are in page: {escape(page)}!"
