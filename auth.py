import flask
from functools import wraps
from db import users, helpers

def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        username = flask.request.cookies.get('username')
        password = flask.request.cookies.get('password')
        if username is None and password is None:
            return flask.redirect(flask.url_for('login.loginscreen'))
        
        db = helpers.load_db()
        user = users.get_user(db, username, password)
        if not user:
            flask.flash('Invalid credentials. Please try again.', 'danger')
            resp = flask.make_response(flask.redirect(flask.url_for('login.loginscreen')))
            resp.set_cookie('username', '', expires=0)
            resp.set_cookie('password', '', expires=0)
            return resp

        flask.username = username
        flask.password = password
        flask.user = user
        return f(*args, **kwargs)
    return decorated_function 