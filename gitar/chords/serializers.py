from chords.models import Genre, Artist, Chord, ArtistGenreReference, ChordGenreReference
from rest_framework import serializers


class ArtistGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistGenreReference
        fields = ("genre_id",)


class ChordGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChordGenreReference
        fields = ("genre_id",)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "genre_name")


class ChordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chord
        fields = ("id", "chord_name", "known_as")


class ChordWithDataSerializer(serializers.ModelSerializer):
    chord_genres = ChordGenreSerializer(many=True)

    class Meta:
        model = Chord
        fields = ("id", "chord_name", "known_as", "chord_data", "chord_genres")


class ArtistSerializer(serializers.ModelSerializer):
    chords = ChordSerializer(many=True)
    artist_genres = ArtistGenreSerializer(many=True)

    class Meta:
        model = Artist
        fields = ("id", "artist_name", "chords", "artist_genres")
