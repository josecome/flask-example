from app import app
from flask import request, make_response

@app.route('/cookies/set')
def set():
    res = make_response({"message":"Cookies set!"})

    res.set_cookie("user", "Test",)

    return res


@app.route('/cookies/get')
def get():
    cookies = request.cookies
    return cookies


@app.route('/cookies/del')
def clear():
    res = make_response({"message":"Cookies deleted!"})

    res.delete_cookie("user")

    return res