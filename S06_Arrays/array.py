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

        return str(list(self.data.values())) + " " + str(self.length)

    ### index verification private method ##############################################################################
    def _checkIndex(self, checkIndex:int) -> None:
        """
        Validates the provided array index.

        Args:
        - checkIndex : int | None, array index to check

        Raises:
        - system exit, if array index is invalid

        Returns:
        - None
        """

        if checkIndex is None or (type(checkIndex) is int and 0 <= checkIndex < self.length): return
        sys.exit(f"{[checkIndex]} Invalid index...\n")
    
    ### insert method ##################################################################################################
    def insert(self, insertIndex:int=None, insertItem:Any=None) -> None:
        """
        Adds a new item to the Array object at the specified position.

        Args:
        - insertIndex : int | None, position where item is inserted, defaults to None
        - insertItem : Any | None, item to be inserted, defaults to None

        Returns:
        - None
        """

        ### validating insert index ------------------------------------------------------------------------------------

        self._checkIndex(checkIndex=insertIndex)
        if insertIndex is None: insertIndex = self.length

        ### insert position occupied > shifting items right ------------------------------------------------------------

        if insertIndex < self.length:
            for index in range(self.length, insertIndex, -1):
                self.data[index] = self.data[index-1]
        
        ### inserting item > updating array length > returning none ----------------------------------------------------

        self.data[insertIndex] = insertItem
        self.length += 1
        return
    
    ### push method ####################################################################################################
    def push(self, pushItem:Any=None) -> None:
        """
        Appends a new item to the end of the Array object.

        Args:
        - pushItem: Any | None, item to be appended, defaults to None

        Returns:
        - self.insert(), result of insert method
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

        self._checkIndex(checkIndex=setIndex)
        self.data[setIndex] = setItem
        return
    
    ### getitem dunder method ##########################################################################################
    def __getitem__(self, getIndex:int) -> Any:
        """
        Defines the [] operator (access) for the Array class.

        Args:
        - getIndex: int, index of item to be returned

        Returns:
        - Any, value of selected item
        """

        self._checkIndex(checkIndex=getIndex)
        return self.data[getIndex]
    
    ### delete method ##################################################################################################
    def delete(self, deleteIndex:int=None) -> Any:
        """
        Removes an item from the Array object at the specified position.

        Args:
        - deleteIndex: int | None, index of item to be deleted, defaults to None

        Returns:
        - deleted_item: Any, value of deleted item | "Empty array...", if array is empty
        """

        ### empty array > returning none -------------------------------------------------------------------------------

        if self.length == 0: return "Empty array..."

        ### validating delete index ------------------------------------------------------------------------------------

        self._checkIndex(checkIndex=deleteIndex)
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
        - self.delete(), result of delete method
        """

        return self.delete()

########################################################################################################################
### testing code
########################################################################################################################

my_array = Array()
print("\nInit:", my_array, "\n")

# print("Check(None):"); my_array._checkIndex(checkIndex=None)
# print("Check('0'):"); my_array._checkIndex(checkIndex='0')
# print("Check(-1):"); my_array._checkIndex(checkIndex=-1)
# print("Check(0):"); my_array._checkIndex(checkIndex=0)
# print("Index OK...\n")

print("Insert():", my_array.insert(), my_array)
print("Insert('Tail'):", my_array.insert(insertItem="Tail"), my_array)
print("Insert(0,'there'):", my_array.insert(insertIndex=0, insertItem="there"), my_array)
print("Insert(0,'Hello'):", my_array.insert(insertIndex=0, insertItem="Hello"), my_array)
print("Insert(2,'sweet'):", my_array.insert(insertIndex=2, insertItem="sweet"), my_array, "\n")
# print("Insert('test','test')", my_array.insert(insertIndex="test", insertItem="test"), my_array, "\n")

print("Push(16):", my_array.push(pushItem=16), my_array)
print("Push('?'):", my_array.push(pushItem="?"), my_array, "\n")

my_array[6] = "!"
print("Set[6] '!':", my_array)
my_array[0] = "Hey"
print("Set[0] 'Hey':", my_array)
my_array[3] = "Joe"
print("Set[3] 'Joe':", my_array, "\n")
# my_array[-3] = "Hi"

print("Get[6]:", my_array[6])
print("Get[0]:", my_array[0])
print("Get[3]:", my_array[3], "\n")
# print("Get[15]:", my_array[15], "\n")

print("Delete():", my_array.delete(), my_array)
print("Delete(0):", my_array.delete(deleteIndex=0), my_array)
print("Delete(3):", my_array.delete(deleteIndex=3), my_array, "\n")
# print("Delete(15):", my_array.delete(deleteIndex=15), my_array, "\n")

print("Pop():", my_array.pop(), my_array)
print("Pop():", my_array.pop(), my_array)
print("Pop():", my_array.pop(), my_array)
print("Pop():", my_array.pop(), my_array)
print("Pop():", my_array.pop(), my_array, "\n")

# my_array[0] = "Hey"
print("Set[0] 'Hey':", my_array)
print("Get[0]:", my_array[0], "\n")
