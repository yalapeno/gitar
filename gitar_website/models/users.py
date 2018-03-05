from sqlalchemy import Column, String
from gitar_website.database import Base
from flask import jsonify


class Users(Base):
    username = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))

    def __repr__(self):
        return f"<User {self.username} {self.email}>"

    def __eq__(self, other):
        return type(self) is type(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def to_json(self):
        return jsonify(dict(name=self.username, email=self.email))


