from app import app
from flask import jsonify

@app.route("/api")
@app.route("/api/<post>")
def api(post='all-posts'):
    return jsonify({"post": post})