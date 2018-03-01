from flask_restful import fields
GENRES_FIELDS = {
    'id': fields.Integer,
    'added': fields.DateTime,
    'name': fields.String
}
