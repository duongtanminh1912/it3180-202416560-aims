import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title, search_by_category


class CategorySearchTests(unittest.TestCase):
    def test_category_exact_case_insensitive(self):
        dvd = DigitalVideoDisc("The Lion King", category="Animation")
        other = DigitalVideoDisc("Star Wars", category="Science Fiction")
        self.assertEqual(search_by_category([dvd, other], "animation"), [dvd])
        self.assertEqual(search_by_category([dvd], "Anim"), [])
        self.assertEqual(search_by_category([], "Animation"), [])


class TitleSearchTests(unittest.TestCase):
    def test_title_substring(self):
        dvd = DigitalVideoDisc("The Lion King")
        self.assertEqual(search_by_title([dvd], "Lion"), [dvd])

    def test_no_match_and_empty_items(self):
        self.assertEqual(search_by_title([DigitalVideoDisc("A")], "Z"), [])
        self.assertEqual(search_by_title([], "Lion"), [])
