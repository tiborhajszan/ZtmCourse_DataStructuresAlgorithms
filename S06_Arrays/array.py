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

        if type(checkIndex) is not int or checkIndex < 0 or self.length <= checkIndex:
            sys.exit("Invalid index...\n")
        return
    
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
    
    ### right shift method #############################################################################################
    def _shiftRight(self, rightIndex=int()) -> None:
        """
        Moves items one position to the right, starting from the specified position up to the end of the array.
        It is used internally to make space for inserting a new item into the array.

        Args:
        - rightIndex: int, position from where items are shifted, defaults to 0
        """

        # iterating through items to be shifted
        for index in range(self.length, rightIndex, -1):
            # shifting item
            self.data[index] = self.data[index-1]
        # returning none
        return
    
    ### insert method ##################################################################################################
    def insert(self, insertItem=None, insertIndex=None) -> int:

        """
        Inserts a new item into the array at the specified position.
        If the position is not specified, the new item is appended to the end of the array.

        Args:
        - insertItem: Any, item to be inserted, defaults to None
        - insertIndex: int|None, position where item is inserted, defaults to None

        Returns:
        - int, new length of array
        """

        # index not specified > assigning array length
        if insertIndex == None: insertIndex = self.length
        # index specified > fixing out of range index
        else: insertIndex = self._checkIndex(checkIndex=insertIndex)
        # insert position occupied > shifting items right
        if insertIndex < self.length: self._shiftRight(rightIndex=insertIndex)
        # inserting item
        self.data[insertIndex] = insertItem
        # updating array length
        self.length += 1
        # returning new array length
        return self.length
    
    ### push method ####################################################################################################
    def push(self, pushItem=None) -> int:
        """
        Appends a new item to the end of the array.

        Args:
        - pushItem: Any, item to be appended, defaults to None

        Returns:
        - int, new length of array
        """

        # inserting item > returning new array length
        return self.insert(insertItem=pushItem)
    
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

# print("Check('0'): ", my_array._checkIndex(checkIndex='0'), "\n")
# print("Check(-1): ", my_array._checkIndex(checkIndex=-1), "\n")
print("Check(0): ", my_array._checkIndex(checkIndex=0), "\n")

# pushing items into array
# new_array.push('Hey')
# new_array.push('there')
# new_array.push('sweet')
# new_array.push(16)
# new_array.push('!')
# print("Push: ", new_array, "\n")
