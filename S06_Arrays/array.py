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
        - checkIndex : int, array index to check

        Returns:
        - bool, True = valid index | False = invalid index
        """

        if type(checkIndex) is not int or checkIndex < -1 or self.length <= checkIndex: return False
        return True
    
    ### insert method ##################################################################################################
    def insert(self, insertIndex:int=-1, insertItem:Any=None) -> None:
        """
        Adds a new item to the Array object at the specified position.

        Args:
        - insertIndex : int, position where item is inserted, defaults to -1
        - insertItem : Any, item to be inserted, defaults to None

        Returns:
        - None
        """

        ### invalid insert index > printing error message > returning none ---------------------------------------------

        if type(insertIndex) is not int or insertIndex < -1 or self.length < insertIndex:
            print(f"Index Error, {repr(insertIndex)} is invalid...")
            return

        ### insert index is -1 > selecting end of array ----------------------------------------------------------------

        if insertIndex == -1: insertIndex = self.length

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
        - pushItem : Any, item to be appended, defaults to None

        Returns:
        - None
        """

        self.insert(insertItem=pushItem)
        return
    
    ### setitem dunder method ##########################################################################################
    def __setitem__(self, setIndex:int, setItem:Any) -> None:
        """
        Defines the assignment [] operator for the Array class.

        Args:
        - setIndex : int, index of item to be updated
        - setItem : Any, new item

        Returns:
        - None
        """

        ### invalid set index > printing error message > returning none ------------------------------------------------

        if not self._checkIndex(checkIndex=setIndex):
            print(f"Index Error, {repr(setIndex)} is invalid...")
            return
        
        ### insert index -1 > selecting last item ----------------------------------------------------------------------

        if setIndex == -1: setIndex = self.length - 1

        ### updating item > returning none -----------------------------------------------------------------------------

        self.data[setIndex] = setItem
        return
    
    ### getitem dunder method ##########################################################################################
    def __getitem__(self, getIndex:int) -> Any:
        """
        Defines the access [] operator for the Array class.

        Args:
        - getIndex : int, index of item to be returned

        Returns:
        - Any, selected item | str, if invalid index
        """

        ### invalid get index > returning error message ----------------------------------------------------------------

        if not self._checkIndex(checkIndex=getIndex):
            return f"Index Error, {repr(getIndex)} is invalid..."
        
        ### get index -1 > selecting last item -------------------------------------------------------------------------

        if getIndex == -1: getIndex = self.length - 1

        ### returning selected item ------------------------------------------------------------------------------------

        return self.data[getIndex]
    
    ### delete method ##################################################################################################
    def delete(self, deleteIndex:int=-1) -> Any:
        """
        Removes an item from the Array object at the specified position.

        Args:
        - deleteIndex : int, index of item to be deleted, defaults to -1

        Returns:
        - deleted_item : Any, deleted item | str, if empty array or invalid index
        """

        ### empty array > returning error message ----------------------------------------------------------------------

        if self.length == 0: return "Empty array..."

        ### invalid delete index > returning error message -------------------------------------------------------------

        if not self._checkIndex(checkIndex=deleteIndex):
            return f"Index Error, {repr(deleteIndex)} is invalid..."

        ### delete index not provided | -1 > selecting last item -------------------------------------------------------

        if deleteIndex == -1: deleteIndex = self.length - 1

        ### recording deleted item > shifting items left ---------------------------------------------------------------

        deleted_item: Any = self.data[deleteIndex]
        for index in range(deleteIndex, self.length-1):
            self.data[index] = self.data[index+1]

        ### deleting item > updating array length > returning deleted item ---------------------------------------------

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

### testing __init__() method ------------------------------------------------------------------------------------------

print("\nInit:", end=" "); my_array = Array(); print(my_array, "\n")

### testing _checkIndex() method ---------------------------------------------------------------------------------------

print("Check('0'):", my_array._checkIndex(checkIndex="0"))
print("Check(-1):", my_array._checkIndex(checkIndex=-1))
print("Check(0):", my_array._checkIndex(checkIndex=0), "\n")

### testing insert() method --------------------------------------------------------------------------------------------

print("Insert(0):", end=" "); my_array.insert(insertIndex=0); print(my_array)
print("Insert('Append'):", end=" "); my_array.insert(insertItem="Append"); print(my_array)
print("Insert(0,'there'):", end=" "); my_array.insert(insertIndex=0, insertItem="there"); print(my_array)
print("Insert(0,'Hello'):", end=" "); my_array.insert(insertIndex=0, insertItem="Hello"); print(my_array)
print("Insert(2,'sweet'):", end=" "); my_array.insert(insertIndex=2, insertItem="sweet"); print(my_array)
print("Insert('test','test'):", end=" "); my_array.insert(insertIndex="test", insertItem="test"); print(my_array, "\n")

### testing push() method ----------------------------------------------------------------------------------------------

print("Push(16):", end=" "); my_array.push(pushItem=16); print(my_array)
print("Push('?'):", end=" "); my_array.push(pushItem="?"); print(my_array, "\n")
sys.exit()

### testing __setitem__() method ---------------------------------------------------------------------------------------

print("Set[-1] '!':", end=" "); my_array[-1] = "!"; print(my_array)
print("Set[0] 'Hey':", end=" "); my_array[0] = "Hey"; print(my_array)
print("Set[3] 'Joe':", end=" "); my_array[3] = "Joe"; print(my_array)
print("Set[-3] 'Hi':", end=" "); my_array[-3] = "Hi"; print(my_array, "\n")

### testing __getitem__() method ---------------------------------------------------------------------------------------

print("Get[-1]:", my_array[-1])
print("Get[0]:", my_array[0])
print("Get[3]:", my_array[3])
print("Get[15]:", my_array[15], "\n")

### testing delete() method --------------------------------------------------------------------------------------------

print("Delete():", my_array.delete(), my_array)
print("Delete(0):", my_array.delete(deleteIndex=0), my_array)
print("Delete(3):", my_array.delete(deleteIndex=3), my_array)
print("Delete(15):", my_array.delete(deleteIndex=15), my_array, "\n")

### testing pop() method -----------------------------------------------------------------------------------------------

print("Pop():", my_array.pop(), my_array)
print("Pop():", my_array.pop(), my_array)
print("Pop():", my_array.pop(), my_array)
print("Pop():", my_array.pop(), my_array)
print("Pop():", my_array.pop(), my_array, "\n")
sys.exit()

print("Set[0] 'Hey':")
my_array[0] = "Hey"
print(my_array)
print("Get[0]:", my_array[0], "\n")
