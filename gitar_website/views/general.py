from flask import Blueprint

from gitar_website.models.chords import Genres

mod = Blueprint("general", __name__)


@mod.route("/")
def index():
    """route for home page."""
    genre = Genres.query.filter_by(id=1).first()
    return genre.to_json()
