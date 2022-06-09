from . import home
from flask import render_template, request, flash, redirect, url_for
from toolz.validators import is_valid_email
from .models import User
import hashlib


@home.route('/')
def home_page():
    return render_template('base.html')


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
    if email == '' or password == '' or username == '' or phone == '':
        flash('All fields are required! ')
        return redirect(url_for('home.sign_up'))
    if password != password2:
        flash('Password does not match')
        return redirect(url_for('home.sign_up'))
    if not is_valid_email(email):
        flash('Please enter a valid email address')
        return redirect(url_for('sign_up'))

    password_hash = hashlib.sha256(password.encode()).hexdigest()
    user_exist = User.query.filter_by(username=username).first()
    if user_exist is not None:
        flash('Username already exists')
        return redirect(url_for('home.sign_up'))

    return redirect(url_for('home.home_page'))


@home.route('/login')
def login():
    return "login"
