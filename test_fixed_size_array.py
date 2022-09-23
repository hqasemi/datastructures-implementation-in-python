from unittest import TestCase

from fixed_size_array import FixedSizeArray


class TestFixedSizeArray(TestCase):
    def setUp(self):
        self.desired_len = 10
        self.obj = FixedSizeArray(self.desired_len)

    def test_len(self):
        self.assertEqual(len(self.obj), self.desired_len)
    
    def test_insertion(self):
        self.obj.insert(0, "Sample")
        self.assertEqual(self.obj[0], "Sample")

    def test_setitem(self):
        self.obj[0] = "Sample"
        self.assertEqual(self.obj[0], "Sample")

    def test_invalid_index_item_insertion(self):
        with self.assertRaises(
                FixedSizeArray.IndexOutOfRangeException
        ):
            self.obj.insert(
                self.desired_len + 1,
                "ShouldNotBeInserted",
            )

