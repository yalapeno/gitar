from django.contrib import admin

from .models import Genre, Chord, Artist

admin.site.register(Genre)
admin.site.register(Chord)
admin.site.register(Artist)
