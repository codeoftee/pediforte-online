from . import home
from flask import render_template, request, flash, redirect, url_for



@home.route('/')
def home_page():
    return "Hello world"


@home.route('/sign-up')
def sign_up():
    return render_template("sign-up.html")

@home.route('/do-sign-up', methods=['POST'])
def do_sign_up():
    username = request.form['username']
    email = request.form['email']
    phone = request.form['phone']
    password = request.form['password']
    password2 = request.form['password2']
    if  email == '' or password == '' or username == '' or phone == '':
        flash('All fields are required! ')
        return redirect(url_for('sign_up'))
    if password != password2:
        flash('Password does not match')
        return redirect(url_for('sign_up'))
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    


@home.route('/login')
def login():
    return "login"
