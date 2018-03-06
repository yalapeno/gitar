from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_login import LoginManager
app = Flask(__name__)
api = Api(app)
login = LoginManager(app)
app.config.from_object("websiteconfig")


from gitar_website.database import db_session, init_db
migrate = Migrate(app, db_session)
init_db()
from gitar_website.test.test_data import populate_database
populate_database.populate()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

from gitar_website.models.users import Users
@login.user_loader
def load_user(id):
    return Users.query.get(int(id))

from gitar_website.views import general
app.register_blueprint(general.mod)

from gitar_website.resources.resources import GenresResource, ArtistChordsResource

api.add_resource(GenresResource, "/genres/<string:id>")
api.add_resource(ArtistChordsResource, "/chords/<string:id>")
