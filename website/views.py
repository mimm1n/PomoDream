from flask import Blueprint, render_template, url_for

views = Blueprint('views', __name__ )

@views.route('/', methods=["GET", "[POST]"])
def home():
    return render_template('base.html')

@views.route('/settings')
def settings():
    return render_template('settings.html')

@views.route('/sign-up')
def sign_up():
    return render_template('sign_up.html')

@views.route('/login')
def login():
    return render_template('login.html')
 