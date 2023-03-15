from typing import Any, Final

from fixed_size_array import FixedSizeArray

INITIAL_ARRAY_SIZE: Final[int] = 0


class DynamicSizeArray:
    """
    This class implements dynamic size array
    """

    class IndexOutOfRangeException(Exception):
        """ Index out of range exception """

    def __init__(self):
        self.__initial_array_size = INITIAL_ARRAY_SIZE
        self.__array = FixedSizeArray(capacity=self.__initial_array_size)
        self.__size = 0

    def insert(self, index: int, value: Any):
        """ Inserts a value to specified index """
        self.__validate_index(index)
        self.__array[index] = value

    def append(self, value: Any):
        """ appends a value to the last index of array """
        if self.__size == self.capacity:
            new_array = FixedSizeArray(capacity=self.__size * 2)
            for index, item in enumerate(self.__array):
                new_array[index] = item

            self.__array = new_array

        self.__array.append(value)
        self.__size = self.__size + 1

    def remove_at(self, index: int) -> None:
        self.__size -= 1
        new_array = FixedSizeArray(self.__size)
        for index in range(0, index):
            new_array[index] = self.__array[index]

        for index in range(index, self.__size):
            new_array[index] = self.__array[index - 1]

        self.__array = new_array

    @property
    def capacity(self) -> int:
        return self.__array.capacity

    def __validate_index(self, index: int):
        if index not in range(self.__size + 1):
            raise self.IndexOutOfRangeException

    def __getitem__(self, key: int):
        return self.__array[key]

    def __setitem__(self, index: int, value: Any):
        self.insert(index, value)

    def __len__(self):
        return self.__size

    def __str__(self):
        return str(self.__array)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__array})"
