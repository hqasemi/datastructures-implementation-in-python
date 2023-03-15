from unittest import TestCase

from dynamic_size_array import DynamicSizeArray


class TestDynamicSizeArray(TestCase):
    def setUp(self):
        self.obj = DynamicSizeArray()

    def test_append(self):
        self.obj.append("Sample")
        self.obj.append("Sample")
        self.obj.append("Sample")

    def test_len(self):
        self.obj.append("Sample")
        self.assertEqual(len(self.obj), 1)
        self.obj.append("Sample")
        self.assertEqual(len(self.obj), 2)
        self.obj.append("Sample")
        self.assertEqual(len(self.obj), 3)

    def test_capacity(self):
        self.assertEqual(self.obj.capacity, 0)

    def test_setitem(self):
        self.obj.append("First Item")
        self.obj.insert(0, "sample")
        self.obj[0] = "Sample"
        self.assertEqual(self.obj[0], "Sample")

    def test_invalid_index_item_insertion(self):
        with self.assertRaises(
                DynamicSizeArray.IndexOutOfRangeException
        ):
            self.obj.insert(
                1,
                "ShouldNotBeInserted",
            )

    def test_remove_at(self):
        self.obj.append("Sample")
        self.obj.append("Sample2")
        self.obj.remove_at(1)
        self.assertEqual(len(self.obj), 1)
