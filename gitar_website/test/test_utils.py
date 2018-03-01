import unittest
from gitar_website.test import TEST_CHORDPRO_LINE
from gitar_website.utils.parsers import ParseChordsPro


class TestUtilities(unittest.TestCase):
    def test_parser(self):
        parser = ParseChordsPro(TEST_CHORDPRO_LINE)
        parsed_line = parser.parse()[0]
        expected = "Am                E                    Am\nBana bir şeyler anlat, canım çok sıkılıyor"
        self.assertEqual(parsed_line, expected)
