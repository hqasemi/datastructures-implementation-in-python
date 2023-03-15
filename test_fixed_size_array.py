from unittest import TestCase

from fixed_size_array import FixedSizeArray


class TestFixedSizeArray(TestCase):
    def setUp(self):
        self.desired_capacity = 10
        self.obj = FixedSizeArray(self.desired_capacity)

    def test_append(self):
        self.obj.append("Sample")
        self.obj.append("Sample")
        self.obj.append("Sample")

    def test_len(self):
        self.obj.append("Sample")
        self.obj.append("Sample")
        self.obj.append("Sample")
        self.assertEqual(len(self.obj), 3)

    def test_capacity(self):
        self.assertEqual(self.obj.capacity, self.desired_capacity)

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
                self.desired_capacity + 1,
                "ShouldNotBeInserted",
            )

    def test_remove_at(self):
        self.obj[0] = "Sample"
        self.obj.append("Sample2")
        self.obj.append("Sample3")
        self.obj.remove_at(1)
        self.assertEqual(len(self.obj), 2)
