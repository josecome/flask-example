from flask import render_template
from markupsafe import escape
from app import app

# Route for Home page and page with dinamic url
@app.route("/")
@app.route("/<page>")
def home(page='no-page-selected'):
    error = None
    return render_template('home.html', page=escape(page), error=error)