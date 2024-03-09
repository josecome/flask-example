from app import app
import os
from flask import send_file

# Define route "/dl".
@app.route("/download")
def download():
    return send_file('files/test.txt', as_attachment=True)