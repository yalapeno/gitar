from chords.models import *

genre1 = Genre(genre_name="genre 1")
genre2 = Genre(genre_name="genre 2")
genre3 = Genre(genre_name="genre 3")
genre1.save()
genre2.save()
genre3.save()

artist1 = Artist(artist_name = "artist name 1")
artist2 = Artist(artist_name = "artist name 2")
artist3 = Artist(artist_name = "artist name 3")
artist4 = Artist(artist_name = "artist name 4") 
artist1.save()
artist2.save()
artist3.save()
artist4.save()

chord1 = Chord(chord_name = "chord name 1", known_as="known as 1", chord_data = {"chord_data_json_key_field":"chord_data_json_value_field_1"}, artist = artist1)
chord2 = Chord(chord_name = "chord name 2", known_as="known as 2", chord_data = {"chord_data_json_key_field":"chord_data_json_value_field_2"}, artist = artist1)
chord3 = Chord(chord_name = "chord name 3", known_as="known as 3", chord_data = {"chord_data_json_key_field":"chord_data_json_value_field_3"}, artist = artist1)
chord4 = Chord(chord_name = "chord name 4", known_as="known as 4", chord_data = {"chord_data_json_key_field":"chord_data_json_value_field_4"}, artist = artist1)
chord5 = Chord(chord_name = "chord name 5", known_as="known as 5", chord_data = {"chord_data_json_key_field":"chord_data_json_value_field_5"}, artist = artist2)
chord6 = Chord(chord_name = "chord name 6", known_as="known as 6", chord_data = {"chord_data_json_key_field":"chord_data_json_value_field_6"}, artist = artist3)
chord7 = Chord(chord_name = "chord name 7", known_as="known as 7", chord_data = {"chord_data_json_key_field":"chord_data_json_value_field_7"}, artist = artist3)
chord8 = Chord(chord_name = "chord name 8", known_as="known as 8", chord_data = {"chord_data_json_key_field":"chord_data_json_value_field_8"}, artist = artist3)
chord9 = Chord(chord_name = "chord name 9", known_as="known as 9", chord_data = {"chord_data_json_key_field":"chord_data_json_value_field_9"}, artist = artist3)
chord10 = Chord(chord_name = "chord name 10", known_as="known as 10", chord_data = {"chord_data_json_key_field":"chord_data_json_value_field_10"}, artist = artist3)
# no chords for artist4

chord1.save()
chord2.save()
chord3.save()
chord4.save()
chord5.save()
chord6.save()
chord7.save()
chord8.save()
chord9.save()
chord10.save()


ag1 = ArtistGenreReference(artist = artist1, genre = genre1)
ag2 = ArtistGenreReference(artist = artist2, genre = genre1)
ag3 = ArtistGenreReference(artist = artist2, genre = genre2)
ag4 = ArtistGenreReference(artist = artist2, genre = genre3)
#no genres for artist3 and 4
ag1.save()
ag2.save()
ag3.save()
ag4.save()

cg1 = ChordGenreReference(chord = chord1, genre = genre1)
cg2 = ChordGenreReference(chord = chord2, genre = genre1)
cg3 = ChordGenreReference(chord = chord3, genre = genre1)
cg4 = ChordGenreReference(chord = chord2, genre = genre2)
cg5 = ChordGenreReference(chord = chord4, genre = genre2)
cg6 = ChordGenreReference(chord = chord5, genre = genre2)
cg7 = ChordGenreReference(chord = chord6, genre = genre3)
cg8 = ChordGenreReference(chord = chord7, genre = genre3)
cg9 = ChordGenreReference(chord = chord8, genre = genre3)
cg10 = ChordGenreReference(chord = chord1, genre = genre3)
# no genres for chord9 and 10

cg1.save()
cg2.save()
cg3.save()
cg4.save()
cg5.save()
cg6.save()
cg7.save()
cg8.save()
cg9.save()
cg10.save()



