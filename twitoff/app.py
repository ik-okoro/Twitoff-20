"""
Main app/routing file for Twitoff
"""

from os import getenv
from flask import Flask, render_template
from .models import DB, User


# Creates application
def create_app():
    """
    Creating and configuring an instance of the Flask application
    """
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URL"] = getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    DB.init_app(app)

    @app.route('/')
    def root():
        #insert_example_users()
        return render_template('base.html', title = "Home", users = User.query.all())
    
    @app.route('/update')
    def update():
        #insert_example_users()
        return render_template('base.html', title="Home", users=Users.query.all())

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title = "Home")

    return app