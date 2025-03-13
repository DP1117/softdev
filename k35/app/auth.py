from flask import session, redirect, url_for
from functools import wraps
from app.db_functions import get_user_by_email

def login_user(user):
    session['user_id'] = user.id
    session['username'] = user.username

def logout_user():
    session.pop('user_id', None)
    session.pop('username', None)

def current_user():
    user_id = session.get('user_id')
    if user_id:
        return get_user_by_email(user_id)
    return None

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user():
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function
