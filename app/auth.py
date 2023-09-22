from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from .models import User  # Import the User model
from . import db  # Import the database instance
from flask_login import login_required, login_user, logout_user, current_user
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(username=email).first()  # Query by email
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect Password", category='error')
        else:
            return redirect(url_for('auth.signup'))
    return render_template('login.html')

@auth.route('/signup', methods=['POST', 'GET'])  # Fix the method typo
def signup():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        password2 = request.form.get('password1')
        print(password)
        print(password2)
        if password != password2:
            flash("Passwords do not match")
            return redirect(url_for('auth.signup'))
        user = User.query.filter_by(username=email).first()  # Query by email
        if not user:
            new_user = User(username=email, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()  # Commit changes to the database
            return redirect(url_for('auth.login'))
        else:
            flash('Email already exists', category='error')
    return render_template('signup.html')

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))