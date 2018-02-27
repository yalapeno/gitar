from flask import Flask
app = Flask(__name__)
app.config.from_object("websiteconfig")


from gitar_website.database import db_session, init_db
init_db()
from gitar_website.test.test_data import populate_database
populate_database.populate()


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


from gitar_website.views import general
app.register_blueprint(general.mod)

