from Flask_app import app
from flask import render_template, redirect, session, flash
from Flask_app.models.user import User

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login')
def r_login():
    if session:
        data = session
    else:
        data = {
            'first_name': '',
            'last_name': '',
            'email': ''
        }
    return render_template('login.html', info = data)

@app.route('register')
def f_register():
    # validate info
    # add to data base
    # login
    return redirect('/home')

@app.route('f-login')
def f_login():
    # pull account
    # login
    return redirect('/home')

@app.route('/logout')
def logout():
    # clear session
    # redirect to home page
    pass