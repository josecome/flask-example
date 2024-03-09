from flask import render_template
from app import app

# Route for Home page
@app.route("/")
def home():
    return render_template('home.html')