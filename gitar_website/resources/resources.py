from flask_restful import Resource, marshal_with, abort
from gitar_website.resources import GENRES_FIELDS
from gitar_website.models.chords import Genres


class GenresResource(Resource):
    @marshal_with(GENRES_FIELDS)
    def get(self,id):
        genre = Genres.query.filter_by(id=id).first()
        if not genre:
            abort(404, message=f"Genre with id {id} doesn't exist")
        return genre





