from dataclasses import dataclass
from typing import Any, Final, List, Optional

from fixed_size_array import FixedSizeArray


Array = FixedSizeArray

@dataclass
class HashTableItem:
    """ Holds hash table items """
    key: Any
    value: Any


class HashTable:
    """ This class is a simple implementation of hash table data structure """
    TABLE_SIZE: Final[int] = 1000

    def __init__(self):
        self.__table: Array = Array(self.TABLE_SIZE)

    def add(self, key: Any, value: Any):
        """ Adds a new item to hash table """
        new_item_index: int = self.__get_index_in_table(key)
        self.__add_by_index(HashTableItem(key, value), new_item_index)

    def __add_by_index(self, item: HashTableItem, index: int) -> None:
        holder_list: Optional[List] = self.__table[index]

        if not holder_list:
            self.__table[index] = [item]
            return

        holder_list.append(item)
        self.__table[index] = holder_list

    def get(self, key: Any) -> Any:
        """ Gets an item's value by it's corresponding key """
        item_index: int = self.__get_index_in_table(key)
        found_value = self.__find_value(item_index, key)
        return found_value

    @classmethod
    def __get_index_in_table(cls, key: Any) -> int:
        hash_value: int = cls.__calculate_hash(key)
        return hash_value % cls.TABLE_SIZE

    @classmethod
    def __calculate_hash(cls, key: any) -> int:
        hash_value: int = hash(key)
        return hash_value

    def __find_value(self, index: int, key: Any) -> Any:
        item_list = self.__get_item_list(index)
        found_value = self.__find_value_in_list(item_list, key)
        return found_value

    def __get_item_list(self, item_index) -> Optional[List]:
        try:
            current_list = self.__table[item_index]
            return current_list
        except AttributeError:
            return None

    @staticmethod
    def __find_value_in_list(current_list: Optional[List], key: Any):
        if not current_list:
            return None

        for item in current_list:
            if item.key == key:
                return item.value

        return None

    def __getitem__(self, key: Any) -> Any:
        return self.get(key)

    def __setitem__(self, key: Any, value: Any):
        self.add(key, value)

