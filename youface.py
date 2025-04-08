# std imports
import time
import os

# installed imports
import flask
import timeago
import tinydb

# handlers
from handlers import friends, login, posts, copy
from auth import auth_required


app = flask.Flask(__name__)

@app.template_filter('convert_time')
def convert_time(ts):
    """A jinja template helper to convert timestamps to timeago."""
    return timeago.format(ts, time.time())

        
        
def register_templates(app):
    """Dynamically registers all HTML templates in a folder as routes.

    Args:
        app: The Flask application instance.
        template_folder: The path to the folder containing the HTML templates.
    """
    for file in os.listdir("templates"):
        if (file == 'base.html'):
            continue
        if (not "_page" in file):
            continue

        if file.endswith(".html"):
            route_name = file[:-5]  # Remove ".html"
            route_path = '/' + file.replace('_page.html', '')

            @auth_required
            def view_func(*args, **kwargs):
                username = flask.username
                user = flask.user

                first_name = user['first_name']
                last_name = user['last_name']
                iq = user['iq']
                friends = len(user['friends'])
                points = user['points'] 

                

                file = flask.request.path.replace('/', '') + "_page.html"
                
                return flask.render_template(file, title=copy.title,
                        subtitle=copy.subtitle, user=user, username=username, first_name=first_name, last_name=last_name, friends=friends, iq=iq, points=points)

            view_func.__name__ = route_name  # Give the view function a name

            app.add_url_rule(route_path, view_func.__name__, view_func)


register_templates(app)


app.register_blueprint(friends.blueprint)
app.register_blueprint(login.blueprint)
app.register_blueprint(posts.blueprint)

app.secret_key = 'mygroup'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.run(debug=True, host='0.0.0.0')
