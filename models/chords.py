from sqlalchemy import Column, Integer, String

from gitar_website.database import Base


class Artist(Base):#table for info about artists
    __tablename__= "artists"
    id = Column(Integer, primary_key=True)#the id of the artist in the database
    name = Column(String(100))#name and surname of the artist

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return f"<Artist {self.name}>"

    def to_json(self):
        return dict(name=self.name)

    def __eq__(self, other):
        return type(self) is type(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)


