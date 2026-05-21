from flask import Blueprint, render_template, request, redirect, flash, session
from config.db import mongo
import bcrypt

auth = Blueprint('auth', __name__)

# Register
@auth.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        existing_user = mongo.db.users.find_one({
            "email": email
        })

        if existing_user:
            flash("Email already exists", "danger")
            return redirect('/register')

        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'),
            bcrypt.gensalt()
        )

        mongo.db.users.insert_one({
            "name": name,
            "email": email,
            "password": hashed_password
        })

        flash("Registration Successful", "success")

        return redirect('/login')

    return render_template('register.html')


# Login
@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')

        user = mongo.db.users.find_one({
            "email": email
        })

        if user:

            if bcrypt.checkpw(
                password.encode('utf-8'),
                user['password']
            ):

                session['user_id'] = str(user['_id'])
                session['user_name'] = user['name']

                flash("Login Successful", "success")

                return redirect('/dashboard')

        flash("Invalid Email or Password", "danger")

        return redirect('/login')

    return render_template('login.html')


# Logout
@auth.route('/logout')
def logout():

    session.clear()

    flash("Logged Out Successfully", "warning")

    return redirect('/')