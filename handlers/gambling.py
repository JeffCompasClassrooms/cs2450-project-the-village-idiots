import flask

from handlers import copy
from db import posts, users, helpers

blueprint = flask.Blueprint("gambling", __name__)
@blueprint.route('/gambling')
def index():
    """Serves the main feed page for the user."""
    db = helpers.load_db()

    # make sure the user is logged in
    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')
    if username is None and password is None:
        return flask.redirect(flask.url_for('login.loginscreen'))
    user = users.get_user(db, username, password)
    if not user:
        flask.flash('Invalid credentials. Please try again.', 'danger')
        resp = flask.make_response(flask.redirect(flask.url_for('login.loginscreen')))
        resp.set_cookie('username', '', expires=0)
        resp.set_cookie('password', '', expires=0)
        return resp

    return flask.render_template('gambling.html', title=copy.title,
            subtitle=copy.subtitle, user=user, username=username,
            games=True)