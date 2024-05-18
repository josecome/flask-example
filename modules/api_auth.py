from flask import Flask, request
from flask import jsonify

from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies

from app import app
from .db_conn import mysql

# Here you can globally configure all the ways you want to allow JWTs to
# be sent to your web application. By default, this will be only headers.
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]

# If true this will only allow the cookies that contain your JWTs to be sent
# over https. In production, this should always be set to True
app.config["JWT_COOKIE_SECURE"] = False

# Change this in your code!
app.config["JWT_SECRET_KEY"] = "super-secret"

jwt = JWTManager(app)


@app.route("/api_login", methods=["POST"])
def api_login():
    username = request.form['username']
    password = request.form['password']
    if all(v is not None for v in [username, password]):
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id,username FROM users WHERE username = %s AND password = %s', (username, password,))
        account = cursor.fetchone()
        if account:
            access_token = create_access_token(identity="example_user")
            return jsonify(access_token=access_token)
        else:
            return 'Invalid Credentials: Please check your username and password and try again'
    else:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT token FROM tokens WHERE token = %s AND expire_date > CURDATE()', (access_token,))
        account = cursor.fetchone()
        if account:
            return jsonify(access_token=access_token)
        else:
            return 'Invalid Credentials: Please check your username and password and try again'
 

def delete_token(token):
    pass


@app.route("/api_logout", methods=["POST"])
def api_logout():
    response = jsonify({"msg": "logout successful"})
    headers = request.headers
    bearer = headers.get('Authorization')    # Bearer YourTokenHere
    token = bearer.split()[1]
    print('=====================Token=================================')
    print(token)
    print('====================End Token===============================')
    delete_token(token)

    return response


@app.route("/protected", methods=["GET", "POST"])
@jwt_required()
def protected():
    return jsonify(foo="bar")
