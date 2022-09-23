from unittest import TestCase

from hash_table import HashTable


class TestHashTable(TestCase):

    def setUp(self):
        self.obj = HashTable()

    def test_set_and_get_item(self):
        self.obj["name"] = "Hesam"
        self.assertEqual(self.obj["name"], "Hesam")

    def test_set_and_get_non_string_key(self):
        self.obj[123] = "test_string"
        self.assertEqual(self.obj[123], "test_string")

    def test_set_and_get_two_items(self):
        self.obj["name"] = "Hesam"
        self.obj["family"] = "Ghasemi"

        self.assertEqual(self.obj["name"], "Hesam")
        self.assertEqual(self.obj["family"], "Ghasemi")

