from flask_restful import Resource, marshal_with, abort
from gitar_website.resources import GENRES_FIELDS, ARTIST_CHORDS_FIELDS
from gitar_website.models.chords import Genres, Artists


class GenresResource(Resource):
    @marshal_with(GENRES_FIELDS)
    def get(self,id):
        genre = Genres.query.filter_by(id=id).first()
        if not genre:
            abort(404, message=f"Genre with id {id} doesn't exist")
        return genre


class ArtistChordsResource(Resource):
    """All chords for an artist. Doesn't include the chord_data field. It's needed when the Chord is displayed"""
    @marshal_with(ARTIST_CHORDS_FIELDS)
    def get(self, id):
        artist = Artists.query.get(id)
        if not artist:
            abort(404, message=f"Artist with id {id} doesn't exist")
        chords = artist.chords.all()
        return chords
