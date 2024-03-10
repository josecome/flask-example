from flask import render_template, session
from app import app

# Route for Home page
@app.route("/")
def home():
    if 'username' in session:
        return render_template('home.html')    
    return "You are not logged in, <a href='/login'>Login</a>"
    