from typing import Any, List


class FixedSizeArray:
    """
    This class implements fixed-size array, as python does not have
    a build-in fixed array implementation
    """

    class IndexOutOfRangeException(Exception):
        """ Index out of range exception """

    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__array = self.__get_an_empty_array(self.__capacity)
        self.__size = 0

    @staticmethod
    def __get_an_empty_array(capacity: int) -> List[Any]:
        return [None] * capacity

    def insert(self, index: int, value: Any):
        """ Inserts a value to the specified index """
        self.__validate_index(index)
        self.__array[index] = value
        self.__size += 1

    def append(self, value: Any):
        """ appends a value to the last index of array """
        self.__array.append(value)
        self.__size += 1

    def remove_at(self, index: int) -> None:
        new_array = self.__get_an_empty_array(self.__capacity)
        for index in range(0, index):
            new_array[index] = self.__array[index]

        for index in range(index, self.__size):
            new_array[index] = self.__array[index - 1]

        self.__array = new_array
        self.__size -= 1

    @property
    def capacity(self):
        return self.__capacity

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
        return f"{self.__class__.__name__}({self.__capacity})"
