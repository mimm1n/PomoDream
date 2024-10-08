from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__ )

@views.route("/")
def landing():
    return render_template('base.html', user=current_user)

@views.route('/settings')
@login_required
def settings():
    return render_template('settings.html', user=current_user)

@views.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@views.route('/home')
def home():
    return render_template('pomo.html', user=current_user)
 
@views.route('/game')
@login_required
def game():
    return render_template('game.html', user=current_user)
