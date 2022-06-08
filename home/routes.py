from . import home
from datetime import timedelta
from flask import render_template, request, flash, session, redirect, url_for
import hashlib
from werkzeug.utils import secure_filename
from models import User

@home.route('/')
def home_page():
    return "Hello world"


@home.route('/sign_up')
def sign_up():
    return "sign up"


@home.route('/login')
def login():
    email = request.form['email']
    password = request.form['password']
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    correct_user = User.query.filter_by(email=email).first()
    if correct_user is not None:
        if correct_user.password_hash == password_hash:
            flash("Welcome " + correct_user.firstname)
            # save session 
            session['email'] = email
            session['password'] = password
            session['id'] = correct_user.id
            
            response = redirect(url_for('admin_page'))
            response.set_cookie('user_id', str(correct_user.id),
                                max_age=timedelta(hours=24))
            response.set_cookie('pw', password_hash,
                                max_age=timedelta(hours=24))
            return response

    flash("Invalid email or password")
    return redirect(url_for('login_page'))