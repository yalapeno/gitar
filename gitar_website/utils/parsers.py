#  TODO: write a parser for guitar lyrics with cords. example in formats/sample_guitar_chord.txt
#  The fonts used in displaying the chords should be so called a "monospaced font",
#  in which the letters occupy equal horizontal space.

# from gitar_website.test.test_data import TEST_LYRICS
# from gitar_website.utils import CHORD_FORMAT_PATTERN
# under dev. 
from re import finditer, sub
TEST_LYRICS = """[Am]Bana bir şeyler an[E]lat, canım çok sıkılı[Am]yor
[Am]Bana bir şeyler anlat an[Dm]lat, [E]içim içimden geçi[Am]yor
[Am]Yanımdasın susu[Dm]yorsun, susuyor konuşmu[E]yorsun
[E]Bakıyor görmü[Am]yorsun

[Am]Dokunsan donaca[E]ğım
[E]İçimde intihar kor[Am]kusu var
[Am]Bir gülsen ağlayaca[Dm]ğım bir gülsen
[E]Kendimi bulaca[Am]ğım"""
CHORD_FORMAT_PATTERN = "\[[^\]]*\]"


def parse_chord(lyrics=TEST_LYRICS):
    lines = lyrics.strip().split("\n")
    res = []
    whitespace = " "
    for line in lines:
        shift = 0
        positions = [(m.start(0), m.end(0), m.group(0)) for m in finditer(CHORD_FORMAT_PATTERN, line)]
        chord_line = ""
        lyrics_line = sub(CHORD_FORMAT_PATTERN, "", line)

        for (position_start, position_end, chord) in positions:
            #position_start -= shift
            #shift += (position_end - position_start)-2
            if position_start<0:
                position_start = 0
            chord_line += f"{whitespace*position_start}{chord.strip('[]')}"
        print(chord_line)
        print(lyrics_line)
    #print(lines)

parse_chord()
