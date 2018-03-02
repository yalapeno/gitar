from gitar_website.database import db_session
from gitar_website.models.chords import *


def populate():
    chord_data = {"chords": """[Am]Bana bir şeyler an[E]lat, canım çok sıkılı[Am]yor
    [Am]Bana bir şeyler anlat an[Dm]lat, [E]içim içimden geçi[Am]yor
    [Am]Yanımdasın susu[Dm]yorsun, susuyor konuşmu[E]yorsun
    [E]Bakıyor görmü[Am]yorsun

    [Am]Dokunsan donaca[E]ğım
    [E]İçimde intihar kor[Am]kusu var
    [Am]Bir gülsen ağlayaca[Dm]ğım bir gülsen
    [E]Kendimi bulaca[Am]ğım""", "bpm": "77"}

    genre_1 = Genres(name="Halk Muzigi")
    artist_1 = Artists(name="Ahmet Kaya")
    genre_ref_1 = ArtistGenreReferences(artist_id=1, genre_id=1)
    chords_1 = Chords(name="İçimde Ölen Biri Var", known_as="Depremler Oluyor Beynimde", chord_data=chord_data, artist_id=1)
    chord_genre_1 = ChordGenreReferences(chord_id=1, genre_id=1)
    db_session.add(genre_1)
    db_session.commit()
