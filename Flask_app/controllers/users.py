from Flask_app import app
from flask import render_template, redirect, session, request
from Flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

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
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': bcrypt.generate_password_hash(request.form['password'])
        }
        session['user_id'] = User.add_user(data)
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
    session.clear()
    return redirect('/login')

@app.route('/home')
def r_home():
    id = session['user_id']
    return render_template('home.html', id = id)