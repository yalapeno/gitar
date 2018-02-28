#  TODO: write a parser for guitar lyrics with cords. example in formats/sample_guitar_chord.txt
#  The fonts used in displaying the chords should be so called a "monospaced font",
#  in which the letters occupy equal horizontal space.

# from gitar_website.test.test_data import TEST_LYRICS
# from gitar_website.utils import CHORD_FORMAT_PATTERN
# under dev.
from re import finditer, sub
TEST_LYRICS = """[Am]Bana bir seyler an[E]lat, canim cok sikili[Am]yor"""

"""[Am]Bana bir şeyler anlat an[Dm]lat, [E]içim içimden geçi[Am]yor
[Am]Yanımdasın susu[Dm]yorsun, susuyor konuşmu[E]yorsun
[E]Bakıyor görmü[Am]yorsun

[Am]Dokunsan donaca[E]ğım
[E]İçimde intihar kor[Am]kusu var
[Am]Bir gülsen ağlayaca[Dm]ğım bir gülsen
[E]Kendimi bulaca[Am]ğım"""
CHORD_FORMAT_PATTERN = "\[[^\]]*\]"
lyrics = TEST_LYRICS
#def parse_chord(lyrics=TEST_LYRICS):
lines = lyrics.strip().split("\n")
res = []
whitespace = " "

with open("deneme.txt", "w") as f:
    for line in lines:
        positions = [(m.start(0), m.end(0), m.group(0)) for m in finditer(CHORD_FORMAT_PATTERN, line)]
        chord_line = ""
        lyrics_line = sub(CHORD_FORMAT_PATTERN, "", line)
        last_end = 0
        last_length = 0
        for (position_start, position_end, chord) in positions:
            chord_line += f"{(whitespace *(position_start - last_end - last_length))}{chord.strip('[]')}"
            last_
            end = position_end
            last_length = len(chord) - 2
        f.write(chord_line + "\n")
        f.write(lyrics_line + "\n")
    #print(lines)

print(open("deneme.txt", "r").read())

#0Am16E20Am
