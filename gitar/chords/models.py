from django.db import models
from django.utils import timezone
# this mysql json field is just for now.
# django supports postgresql json field
# use that when switching to postgresql
# from django.contrib.postgres.fields import JSONField
from django_mysql.models import JSONField


class GitarBase(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if not self.id:  # when the id has not been set yet, meaning when it's first created
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(GitarBase, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Genre(GitarBase):
    genre_name = models.CharField(max_length=64)

    def __str__(self):
        return self.genre_name


class Artist(GitarBase):
    artist_name = models.CharField(max_length=128)

    def __str__(self):
        return self.artist_name


class ArtistGenreReference(GitarBase):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="artist_genres")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class Chord(GitarBase):
    chord_name = models.CharField(max_length=128)
    known_as = models.CharField(max_length=64)
    chord_data = JSONField()
    artist = models.ForeignKey(Artist, on_delete=models.SET_DEFAULT, default=None, related_name="chords")

    def __str__(self):
        return self.chord_name


class ChordGenreReference(GitarBase):
    chord = models.ForeignKey(Chord, on_delete=models.CASCADE, related_name="chord_genres")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
