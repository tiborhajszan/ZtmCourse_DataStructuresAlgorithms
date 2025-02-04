########################################################################################################################
### Data Structures and Algorithms :: Section 06
### Lesson: Implementing An Array
########################################################################################################################

### imports ------------------------------------------------------------------------------------------------------------

import sys
from typing import Dict, Any

########################################################################################################################
### MyArray Class
########################################################################################################################
class Array:
    """
    Implements a basic one-dimensional array data structure.

    Attributes:
    - length: int, length of array
    - data: dict, container to store array data
    """

    ### constructor method #############################################################################################
    def __init__(self) -> None:
        """
        Initializes a new empty Array object.

        Args:
        - None

        Attributes:
        - data : Dict[int,Any], container to store array data, defaults to empty dictionary
        - length : int, length of array, defaults to 0

        Returns:
        - None
        """

        self.data: Dict[int,Any] = dict()
        self.length: int = int(0)
        return
    
    ### str dunder method ##############################################################################################
    def __str__(self) -> str:
        """
        Defines the string representation for the Array class.

        Args:
        - None

        Returns:
        - str, string representation of Array class
        """

        return f"{list(self.data.values())} {self.length}"

    ### index verification private method ##############################################################################
    def _checkIndex(self, checkIndex:int) -> bool:
        """
        Validates the provided array index.

        Args:
        - checkIndex : int | None, array index to check

        Returns:
        - bool, True = valid index | False = invalid index
        """

        if checkIndex is None or (type(checkIndex) is int and 0 <= checkIndex < self.length): return True
        return False
    
    ### insert method ##################################################################################################
    def insert(self, insertIndex:int=None, insertItem:Any=None) -> str:
        """
        Adds a new item to the Array object at the specified position.

        Args:
        - insertIndex : int | None, position where item is inserted, defaults to None
        - insertItem : Any | None, item to be inserted, defaults to None

        Returns:
        - str, "OK" if insert successful | str, result of _checkIndex() method if invalid index
        """

        ### invalid insert index > returning error message -------------------------------------------------------------

        check_result: str = self._checkIndex(checkIndex=insertIndex)
        if 0 < len(check_result): return check_result

        ### insert index not provided > appending to end of array ------------------------------------------------------

        if insertIndex is None: insertIndex = self.length

        ### insert position occupied > shifting items right ------------------------------------------------------------

        if insertIndex < self.length:
            for index in range(self.length, insertIndex, -1):
                self.data[index] = self.data[index-1]
        
        ### inserting item > updating array length > returning OK ------------------------------------------------------

        self.data[insertIndex] = insertItem
        self.length += 1
        return "OK"
    
    ### push method ####################################################################################################
    def push(self, pushItem:Any=None) -> str:
        """
        Appends a new item to the end of the Array object.

        Args:
        - pushItem : Any | None, item to be appended, defaults to None

        Returns:
        - str, result of insert() method
        """

        return self.insert(insertItem=pushItem)
    
    ### setitem dunder method ##########################################################################################
    def __setitem__(self, setIndex:int, setItem:Any=None) -> None:
        """
        Defines the [] operator (assignment) for the Array class.

        Args:
        - setIndex : int, index of item to be updated
        - setItem : Any | None, update item, defaults to None

        Returns:
        - None
        """

        ### invalid set index > printing error message > returning none ------------------------------------------------

        check_result: str = self._checkIndex(checkIndex=setIndex)
        if 0 < len(check_result):
            print(check_result)
            return

        ### updating item > returning none -----------------------------------------------------------------------------

        self.data[setIndex] = setItem
        return
    
    ### getitem dunder method ##########################################################################################
    def __getitem__(self, getIndex:int) -> Any:
        """
        Defines the [] operator (access) for the Array class.

        Args:
        - getIndex : int, index of item to be returned

        Returns:
        - Any, selected item | str, result of _checkIndex() method if invalid index
        """

        ### invalid get index > returning error message ----------------------------------------------------------------

        check_result: str = self._checkIndex(checkIndex=getIndex)
        if 0 < len(check_result): return check_result

        ### returning selected item ------------------------------------------------------------------------------------

        return self.data[getIndex]
    
    ### delete method ##################################################################################################
    def delete(self, deleteIndex:int=None) -> Any:
        """
        Removes an item from the Array object at the specified position.

        Args:
        - deleteIndex : int | None, index of item to be deleted, defaults to None

        Returns:
        - deleted_item : Any, deleted item | str, if empty array or invalid index
        """

        ### empty array > returning error message ----------------------------------------------------------------------

        if self.length == 0: return "Empty array..."

        ### invalid delete index > returning error message -------------------------------------------------------------

        check_result: str = self._checkIndex(checkIndex=deleteIndex)
        if 0 < len(check_result): return check_result

        ### delete index not provided > deleting last item -------------------------------------------------------------

        if deleteIndex == None: deleteIndex = self.length - 1

        ### recording deleted item > shifting items left ---------------------------------------------------------------

        deleted_item: Any = self.data[deleteIndex]
        for index in range(deleteIndex, self.length-1):
            self.data[index] = self.data[index+1]

        ### deleting item > updating array length > returning deleted value --------------------------------------------

        del self.data[self.length-1]
        self.length -= 1
        return deleted_item

    ### pop method #####################################################################################################
    def pop(self) -> Any:
        """
        Removes the last item from the Array object.

        Args:
        - None

        Returns:
        - Any | str, result of delete() method
        """

        return self.delete()

########################################################################################################################
### testing code
########################################################################################################################

### testing constructor method -----------------------------------------------------------------------------------------

my_array = Array()
print("\nInit:", my_array, "\n")

### testing _checkIndex method -----------------------------------------------------------------------------------------

print("Check(None):", my_array._checkIndex(checkIndex=None))
print("Check('0'):", my_array._checkIndex(checkIndex="0"))
print("Check(-1):", my_array._checkIndex(checkIndex=-1))
print("Check(0):", my_array._checkIndex(checkIndex=0), "\n")
sys.exit()

print("Insert():", my_array.insert(), my_array)
print("Insert('Append'):", my_array.insert(insertItem="Append"), my_array)
print("Insert(0,'there'):", my_array.insert(insertIndex=0, insertItem="there"), my_array)
print("Insert(0,'Hello'):", my_array.insert(insertIndex=0, insertItem="Hello"), my_array)
print("Insert(2,'sweet'):", my_array.insert(insertIndex=2, insertItem="sweet"), my_array)
print("Insert('test','test')", my_array.insert(insertIndex="test", insertItem="test"), my_array, "\n")

print("Push(16):", my_array.push(pushItem=16), my_array)
print("Push('?'):", my_array.push(pushItem="?"), my_array, "\n")

print("Set[6] '!':")
my_array[6] = "!"
print(my_array)
print("Set[0] 'Hey':")
my_array[0] = "Hey"
print(my_array)
print("Set[3] 'Joe':")
my_array[3] = "Joe"
print(my_array)
print("Set[-3] 'Hi':")
my_array[-3] = "Hi"
print(my_array, "\n")

print("Get[6]:", my_array[6])
print("Get[0]:", my_array[0])
print("Get[3]:", my_array[3])
print("Get[15]:", my_array[15], "\n")

print("Delete():", my_array.delete(), my_array)
print("Delete(0):", my_array.delete(deleteIndex=0), my_array)
print("Delete(3):", my_array.delete(deleteIndex=3), my_array)
print("Delete(15):", my_array.delete(deleteIndex=15), my_array, "\n")

print("Pop():", my_array.pop(), my_array)
print("Pop():", my_array.pop(), my_array)
print("Pop():", my_array.pop(), my_array)
print("Pop():", my_array.pop(), my_array)
print("Pop():", my_array.pop(), my_array, "\n")

print("Set[0] 'Hey':")
my_array[0] = "Hey"
print(my_array)
print("Get[0]:", my_array[0], "\n")
