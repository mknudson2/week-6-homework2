from flask import render_template, redirect, flash
from collection_app import app
from collection_app.forms import LoginForm
from collection_app.forms import SignupForm
from collection_app.models import User

@app.route('/')
def home():
    return render_template('index.jinja', title='Collection Homepage' )

@app.route('/signin')
def signin():
    loginform = LoginForm()
    if loginform.validate_on_submit():
        email = loginform.email.data
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(loginform.password.data):
            flash(f'{loginform.email.data} has logged in!', category='success')
            return redirect('/')
        else:
            flash(f'Invalid user data. Please try again.', category='warning')
    return render_template('/signin.jinja', title='Sign-In', form = loginform)


@app.route('/register')
def register():
    signupform = SignupForm()
    if signupform.validate_on_submit():
        first_name=signupform.first_name.data
        last_name=signupform.last_name.data
        username=signupform.username.data
        email=signupform.email.data
        try:
            user = User(first_name=first_name, last_name=last_name, username=username, email=email)
            user.hash_password(signupform.password.data)
            user.commit()
            flash(f'Congrats, {first_name}, you have registered!', category='success')
            return redirect('/')
        except:
            flash(f'Sorry! The username or email has already been taken. Please try again.', category='warning')
    return render_template('/register.jinja', title='Sign Up', form=signupform)


# @app.route('display_collection')
# def display_collection():
#     pass