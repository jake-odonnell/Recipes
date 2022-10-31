from Flask_app import app
from flask import render_template, redirect, session, request
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

@app.route('/register', methods = ['POST'])
def f_register():
    if User.val_new_user(request.form):
        session['user_id'] = User.add_user(request.form)
        return redirect('/home')
    else:
        return redirect('/login')

    # add to data base
    # login

@app.route('/f-login')
def f_login():
    # pull account
    # login
    return redirect('/home')

@app.route('/logout')
def logout():
    # clear session
    # redirect to home page
    pass

@app.route('/home')
def r_home():
    return render_template('home.html')