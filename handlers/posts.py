import flask

from db import posts, helpers
from auth import auth_required
blueprint = flask.Blueprint("posts", __name__)

@blueprint.route('/post', methods=['POST'])
@auth_required
def post():
    """Creates a new post."""
    db = helpers.load_db()

    user = flask.user

    post = flask.request.form.get('post')
    posts.add_post(db, user, post)

    return flask.redirect(flask.url_for('login.index'))
