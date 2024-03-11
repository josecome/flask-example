from flask import request, redirect, url_for, session, render_template
from app import app
from .db_conn import mysql

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/login', methods=['GET', 'POST'])
def login():    
    msg = ''
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password'] # c2gx42pwhp9ym4x5p0brniturk834j
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id,username FROM users WHERE username = %s AND password = %s', (username, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            # Redirect to home page
            msg = 'Logged in successfully!'
            return render_template('home.html', msg=msg)
        else:
            msg = 'Invalid Credentials: Please check your username and password and try again'
            return redirect(url_for('login',msg=msg))
        
    return render_template('login.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('home'))