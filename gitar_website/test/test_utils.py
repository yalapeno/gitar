import unittest
from gitar_website.test import TEST_CHORDPRO_LINE
from gitar_website.test import TEST_CHORDPRO_LINE_STARTING_WITH_LYRICS
from gitar_website.test import TEST_CHORDPRO_LINE_STARTING_WITH_TWO_CHORDS
from gitar_website.utils.parsers import ParseChordsPro
from gitar_website.chopro import chopro2html


class TestUtilities(unittest.TestCase):

    def test_parser(self):
        """Test the ChordPro parser."""

        #  if the line starts with a chord
        parser = ParseChordsPro(TEST_CHORDPRO_LINE)
        parsed_line = parser.parse()[0]
        expected = "Am                E                    Am\nBana bir şeyler anlat, canım çok sıkılıyor"
        self.assertEqual(parsed_line, expected)

        #  if the line starts with lyrics
        parser = ParseChordsPro(TEST_CHORDPRO_LINE_STARTING_WITH_LYRICS)
        parsed_line = parser.parse()[0]
        expected = "                  E                    Am\nBana bir şeyler anlat, canım çok sıkılıyor"
        self.assertEqual(parsed_line, expected)

    def test_chopro(self):
        """Test chopro project"""

        # test html chopro2html
        import os
        #  chord_pro_string = open(os.path.abspath("../test/test_data/sample.cho")).read() #debug mode
        file = open(os.path.abspath("gitar_website/test/test_data/sample.cho"))
        chord_pro_string = file.read()
        html_formatted = chopro2html(chord_pro_string, html_style='table')
        file.close()
        #  print(html_formatted)
        del os
