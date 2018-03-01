#  The fonts used in displaying the chords should be so called a "monospaced font",
#  in which the letters occupy equal horizontal space.
from gitar_website.utils import CHORD_FORMAT_PATTERN, WHITE_SPACE
from re import finditer, sub


class ParseChordsPro:
    def __init__(self, chords_pro_string):
        self.chords_pro_string = chords_pro_string  # input
        self.chords_list = []  # the chords used in this song
        self.lines = []  # each element is a lyric line with the chords on right position(2 lines)

    def parse(self):
        lines = self.chords_pro_string.strip().split("\n")

        for line in lines:
            positions = [(m.start(0), m.end(0), m.group(0)) for m in finditer(CHORD_FORMAT_PATTERN, line)]
            chord_line = ""
            lyrics_line = sub(CHORD_FORMAT_PATTERN, "", line)
            last_end = 0
            last_chord_length = 0
            for (position_start, position_end, chord) in positions:
                chord_line += f"{(WHITE_SPACE *(position_start - last_end - last_chord_length))}{chord.strip('[]')}"
                last_end = position_end
                last_chord_length = len(chord) - 2
            self.lines.append(chord_line + "\n" + lyrics_line)
        return self.lines
