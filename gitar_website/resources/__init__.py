from flask_restful import fields
GENRES_FIELDS = {
    'id': fields.Integer,
    'added': fields.DateTime,
    'name': fields.String
}

ARTIST_CHORDS_FIELDS = {
    "id": fields.Integer,
    "name": fields.String,
    "known_as": fields.String
}

CHORD_FIELDS = {
    "id": fields.Integer,
    "name": fields.String,
    "known_as": fields.String,
    "chord_data": fields.Raw,
    "artist_id": fields.Integer
}
