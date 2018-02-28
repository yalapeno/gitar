from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from gitar_website.database import Base
from flask import jsonify


class Genres(Base):
    """table for allowed genres."""
    name = Column(String(64))  # name of the genre.

    def to_json(self):
        return jsonify(dict(name=self.name))

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return f"<Genre {self.name}>"

    def __eq__(self, other):
        return type(self) is type(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)


class Artists(Base):
    """table for info about artists."""
    name = Column(String(128))  # name and surname of the artist.

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return f"<Artist {self.name}>"

    def to_json(self):
        return jsonify(dict(name=self.name))

    def __eq__(self, other):
        return type(self) is type(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)


class GenreReferences(Base):
    """table for music genres of artists. maps artist ids to genre ids."""
    artist_id = Column(Integer, ForeignKey("artists.id"))
    genre_id = Column(Integer, ForeignKey("genres.id"))

    def __init__(self, artist_id=None, genre_id=None):
        self.artist_id = artist_id
        self.genre_id = genre_id


class Chords(Base):
    """table for lyrics with chords"""
    name = Column(String(128))  # name of the song.
    known_as = Column(String(64))  # alternative name for the song.
    chord_data = Column(JSON)  # the chords and other related data to the song.
    artist_id = Column(Integer, ForeignKey("artists.id"))

    def __init__(self, name=None, known_as=None, chord_data=None, artist_id=None):
        self.name = name
        self.known_as = known_as
        self.chord_data = chord_data
        self.artist_id = artist_id

    def __repr__(self):
        return f"<Chord {self.name}>"

    def to_json(self):
        return jsonify(dict(name=self.name))

    def __eq__(self, other):
        return type(self) is type(other) and self.id == other.id

    def __ne__(self, other):
        return not self.__eq__(other)


class ChordGenreReferences(Base):
    """table for music genres of song chords. maps chord ids to genre ids."""
    chord_id = Column(Integer, ForeignKey("chords.id"))
    genre_id = Column(Integer, ForeignKey("genres.id"))

    def __init__(self, chord_id=None, genre_id=None):
        self.chord_id = chord_id
        self.genre_id = genre_id
