from typing import Any


class FixedSizeArray:
    """ 
    This class implemenets fixed-size array, as python does not have 
    a build-in fixed array implementation
    """

    class IndexOutOfRangeException(Exception):
        """ Index out of range exception """

    def __init__(self, array_size: int):
        self.__array_size = array_size
        self.__array = [None] * self.__array_size

    def insert(self, index: int, value: Any):
        """ Inserts a value to specified index """
        self.__validate_index(index)   
        self.__array[index] = value

    def __validate_index(self, index: int):
        if index not in range(self.__array_size):
            raise self.IndexOutOfRangeException

    def __getitem__(self, key: int):
        return self.__array[key]

    def __setitem__(self, key:int ,value: Any):
        self.__validate_index(key)
        self.__array[key] = value

    def __len__(self):
        return self.__array_size
    
    def __str__(self):
        return str(self.__array)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__array_size})"


