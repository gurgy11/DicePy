from flask import current_app, session, redirect, url_for
from flask.globals import request

def authenticate():
    is_authenticated = False
    with current_app.app_context():
        if 'user_id' in session and 'user_username' in session:
            is_authenticated = True
    return is_authenticated

def login_required():
    with current_app.app_context():
        print(request.host_url)
        print(request)
        if authenticate() is not True:
            return redirect(url_for('auth.login_required'))
