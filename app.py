#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request, url_for
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
import os

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    return render_template('pages/placeholder.home.html')


@app.route('/match_list')
def match_list():
    return render_template('pages/match_list.html')


@app.route('/profile')
def profile():
    user = {
        "avatar": url_for('static', filename='img/user.svg'),
        "name": "ME!ME!ME!",
        "interests": "ME!ME!ME!",
        "icebreaker": "this is a boring icebreaker"
    }
    return render_template('pages/my_profile.html', user=user)


@app.route('/user/john')
def john():
    user_john = {
        "avatar": url_for('static', filename='img/john.svg'),
        "name": "John",
        "interests": "HAHA",
        "icebreaker": "I'm a HAHAFAN. I HAHA everyday. I have a infinity life. You need to learn one thing or two."
    }
    return render_template('pages/user_profile.html', user=user_john)


@app.route('/user/jane')
def jane():
    user_jane = {
        "avatar": url_for('static', filename='img/jane.svg'),
        "name": "Jane",
        "interests": "DADADADA",
        "icebreaker": "I'm a DADAFAN. I DADA everyday. I DADA when thonking. I like thonking while DADing."
    }
    return render_template('pages/user_profile.html', user=user_jane)


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.route('/login')
def login():
    form = LoginForm(request.form)
    return render_template('forms/login.html', form=form)


@app.route('/register')
def register():
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)

# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
