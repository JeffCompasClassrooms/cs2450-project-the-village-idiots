import flask
from tinydb import TinyDB, Query
from auth import auth_required

blueprint = flask.Blueprint("points", __name__)
DB_PATH = 'db/users.json'


def get_user_record(username):
    db = TinyDB(DB_PATH)
    User = Query()
    return db, User, db.get(User.username == username)


@blueprint.route('/points/increase/<int:amount>', methods=['POST'])
@auth_required
def increase_points(amount):
    username = flask.username
    db, User, user = get_user_record(username)

    if not user:
        flask.flash("User not found", "danger")
        return flask.redirect(flask.url_for('login.index'))

    current_points = user.get('points', 0)
    new_points = current_points + amount
    db.update({'points': new_points}, User.username == username)
    flask.user['points'] = new_points

    flask.flash(f"You earned {amount} points! Total: {new_points}", "success")
    return flask.redirect(flask.request.referrer or flask.url_for('login.index'))


@blueprint.route('/points/decrease/<int:amount>', methods=['POST'])
@auth_required
def decrease_points(amount):
    username = flask.username
    db, User, user = get_user_record(username)

    if not user:
        flask.flash("User not found", "danger")
        return flask.redirect(flask.url_for('login.index'))

    current_points = user.get('points', 0)
    new_points = max(0, current_points - amount)
    db.update({'points': new_points}, User.username == username)
    flask.user['points'] = new_points

    flask.flash(f"{amount} points spent. Remaining: {new_points}", "warning")
    return flask.redirect(flask.request.referrer or flask.url_for('login.index'))
