from sqlalchemy import Column, Integer, String, ForeignKey
from gitar_website.database import Base


class Genre(Base):
    """table for allowed genres."""
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True)
    name = Column(String(64))  # name of the genre.

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return f"<Genre {self.name}>"

    def to_json(self):
        return dict(name=self.name)

    def __eq__(self, other):
        return type(self) is type(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)


class Artist(Base):
    """table for info about artists."""
    __tablename__ = "artists"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))  # name and surname of the artist.

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


class GenreReference(Base):
    """table for music genres of artists. maps artist ids to genre ids in artists and genres tables."""
    __tablename__ = "genre_reference"
    id = Column(Integer, primary_key=True) # id for the entry. not sure if it's needed.
    artist_id = Column(Integer, ForeignKey("artists.id"))
    genre_id = Column(Integer, ForeignKey("genres.id"))

    def __init__(self, artist_id=None, genre_id=None):
        self.artist_id = artist_id
        self.genre_id = genre_id
