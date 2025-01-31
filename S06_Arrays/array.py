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
        - checkIndex : int, array index to check

        Returns:
        - None
        """

        if checkIndex is None or (type(checkIndex) is int and 0 <= checkIndex < self.length): return
        sys.exit("Invalid index...\n")
    
    ### insert method ##################################################################################################
    def insert(self, insertItem:Any=None, insertIndex:int=None) -> None:
        """
        Adds a new item to the Array object at the specified position.

        Args:
        - insertItem : Any | None, item to be inserted, defaults to None
        - insertIndex : int | None, position where item is inserted, defaults to None

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
        - None
        """

        self.insert(insertItem=pushItem)
        return
    
    ### item set method ################################################################################################
    def set(self, setItem=None, setIndex=None) -> Any:
        """
        Sets the item at the specified position.
        If the position is not specified, the last item is set.

        Args:
        - setItem: Any, item to be set, defaults to None
        - setIndex: int|None, position where item is set, defaults to None

        Returns:
        - Any, new item from array
        """

        # index not specified > assigning last index
        if setIndex == None: setIndex = self.length - 1
        # index specified > fixing out of range index
        else: setIndex = self._checkIndex(checkIndex=setIndex)
        # setting item
        self.data[setIndex] = setItem
        # returning new item from array
        return self.data[setIndex]
    
    ### item access method #############################################################################################
    def get(self, getIndex=None) -> Any:
        """
        Returns the item from the specified position.
        If the position is not specified, the last item is returned.

        Args:
        - getIndex: int|None, position of item to be returned, defaults to None

        Returns:
        - Any, selected item from array
        """

        # index not specified > assigning last index
        if getIndex == None: getIndex = self.length - 1
        # index specified > fixing out of range index
        else: getIndex = self._checkIndex(checkIndex=getIndex)
        # returning item from array
        return self.data[getIndex]
    
    ### left shift method ##############################################################################################
    def _shiftLeft(self, leftIndex=int()) -> None:
        """
        Moves items one position to the left, starting from the specified position up to the end of the array.
        It is used internally to fill the deleted position in the array.

        Args:
        - leftIndex: int, position from where items are shifted, defaults to 0
        """

        # iterating through items to be shifted
        for index in range(leftIndex, self.length - 1):
            # shifting item
            self.data[index] = self.data[index+1]
        # deleting last item
        del self.data[self.length - 1]
        # returning none
        return
    
    ### delete method ##################################################################################################
    def delete(self, deleteIndex=None) -> int:
        """
        Deletes the item at the specified position in the array.
        If the position is not specified, the last item is deleted.

        Args:
        - deleteIndex: int|None, position where item is deleted, defaults to None

        Returns:
        - int, new length of array
        """

        # index not specified > assigning last index
        if deleteIndex == None: deleteIndex = self.length - 1
        #  index specified > fixing out of range index
        else: deleteIndex = self._checkIndex(checkIndex=deleteIndex)
        # clering item
        self.data[deleteIndex] = None
        # shifting items left
        self._shiftLeft(leftIndex=deleteIndex)
        # updating array length
        self.length -= 1
        # returning new array length
        return self.length

    ### pop method #####################################################################################################
    def pop(self) -> int:
        """
        Deletes the last item in the array.

        Returns:
        - int, new length of array
        """

        # deleting item > returning new array length
        return self.delete()

########################################################################################################################
### testing code
########################################################################################################################

my_array = Array()
print("\nInit:", my_array, "\n")

print("Check(None):"); my_array._checkIndex(checkIndex=None)
# print("Check('0'):"); my_array._checkIndex(checkIndex='0')
# print("Check(-1):"); my_array._checkIndex(checkIndex=-1)
# print("Check(0):"); my_array._checkIndex(checkIndex=0)
print("Index OK...\n")

my_array.insert()
print("Insert():", my_array, "\n")
my_array.insert(insertItem="Tail")
print("Insert('Tail'):", my_array, "\n")
my_array.insert(insertItem="there", insertIndex=0)
print("Insert('there', 0):", my_array, "\n")
my_array.insert(insertItem="Hey", insertIndex=0)
print("Insert('Hey', 0):", my_array, "\n")
my_array.insert(insertItem="sweet", insertIndex=2)
print("Insert('sweet', 2):", my_array, "\n")

my_array.push(pushItem=16)
print("Push(16):", my_array, "\n")
my_array.push(pushItem='!')
print("Push('!'):", my_array, "\n")
