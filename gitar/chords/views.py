from chords.models import Genre, Artist, Chord
from rest_framework import viewsets
from chords.serializers import GenreSerializer, ChordSerializer, ArtistSerializer, ChordWithDataSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ChordViewSet(viewsets.ModelViewSet):
    queryset = Chord.objects.all()
    serializer_class = ChordSerializer


class ChordWithDataViewSet(viewsets.ModelViewSet):
    queryset = Chord.objects.all()
    serializer_class = ChordWithDataSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
