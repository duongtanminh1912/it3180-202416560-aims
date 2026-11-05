import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TitleSearchTests(unittest.TestCase):
    def test_title_substring(self):
        dvd = DigitalVideoDisc("The Lion King")
        self.assertEqual(search_by_title([dvd], "Lion"), [dvd])

    def test_no_match_and_empty_items(self):
        self.assertEqual(search_by_title([DigitalVideoDisc("A")], "Z"), [])
        self.assertEqual(search_by_title([], "Lion"), [])

    def test_lowercase_keyword_matches_title(self):
        dvd = DigitalVideoDisc("The Lion King")
        self.assertEqual(search_by_title([dvd], "lion"), [dvd])
        self.assertEqual(search_by_title([dvd], "LION"), [dvd])
