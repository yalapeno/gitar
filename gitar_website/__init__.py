from flask import Flask
app = Flask(__name__)
app.config.from_object("websiteconfig")

from gitar_website.database import db_session, init_db



@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


