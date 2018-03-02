from flask import Flask
from flask_restful import Api
app = Flask(__name__)
api = Api(app)
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

from gitar_website.resources.resources import GenresResource

api.add_resource(GenresResource, "/genres/<string:id>")
