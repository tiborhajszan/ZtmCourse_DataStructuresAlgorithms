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
    
    ### insert method ##################################################################################################
    def insert(self, insertIndex:int=-1, insertValue:Any=None) -> None:
        """
        Adds a new item to the Array object at the specified position.

        Args:
        - insertIndex : int, position where item is inserted, defaults to -1
        - insertValue : Any, value of inserted item, defaults to None

        Returns:
        - None
        """

        ### invalid insert index > printing error message > returning none ---------------------------------------------

        if type(insertIndex) is not int or insertIndex < -1 or self.length <= insertIndex:
            print(f"Index Error, {repr(insertIndex)} is invalid...")
            return

        ### insert index is -1 > selecting end of array ----------------------------------------------------------------

        if insertIndex == -1: insertIndex = self.length

        ### insert position occupied > shifting items right ------------------------------------------------------------

        if insertIndex < self.length:
            for index in range(self.length, insertIndex, -1):
                self.data[index] = self.data[index-1]
        
        ### inserting item > updating array length > returning none ----------------------------------------------------

        self.data[insertIndex] = insertValue
        self.length += 1
        return
    
    ### push method ####################################################################################################
    def push(self, pushValue:Any=None) -> None:
        """
        Appends a new item to the end of the Array object.

        Args:
        - pushValue : Any, value of appended item, defaults to None

        Returns:
        - None
        """

        self.insert(insertValue=pushValue)
        return
    
    ### setitem dunder method ##########################################################################################
    def __setitem__(self, setIndex:int, setValue:Any) -> None:
        """
        Defines the assignment [] operator for the Array class.

        Args (signature):
        - setIndex : int, index of item to be updated
        - setValue : Any, new value of updated item

        Returns:
        - None
        """

        ### invalid set index > printing error message > returning none ------------------------------------------------

        if type(setIndex) is not int or setIndex < 0 or self.length <= setIndex:
            print(f"Index Error, {repr(setIndex)} is invalid...")
            return

        ### updating item > returning none -----------------------------------------------------------------------------

        self.data[setIndex] = setValue
        return
    
    ### getitem dunder method ##########################################################################################
    def __getitem__(self, getIndex:int) -> Any:
        """
        Defines the access [] operator for the Array class.

        Args:
        - getIndex : int, index of item to be returned

        Returns:
        - Any, value of selected item | str, if invalid index
        """

        ### invalid get index > returning error message ----------------------------------------------------------------

        if type(getIndex) is not int or getIndex < 0 or self.length <= getIndex:
            return f"Index Error, {repr(getIndex)} is invalid..."

        ### returning value of selected item ---------------------------------------------------------------------------

        return self.data[getIndex]
    
    ### delete method ##################################################################################################
    def delete(self, deleteIndex:int=-1) -> Any:
        """
        Removes an item from the Array object at the specified position.

        Args:
        - deleteIndex : int, index of item to be deleted, defaults to -1

        Returns:
        - deleted_item : Any, value of deleted item | str, if empty array or invalid index
        """

        ### empty array | invalid delete index > returning error message -----------------------------------------------

        if self.length == 0:
            return "Empty array..."
        if type(deleteIndex) is not int or deleteIndex < -1 or self.length <= deleteIndex:
            return f"Index Error, {repr(deleteIndex)} is invalid..."

        ### delete index is -1 > selecting last item -------------------------------------------------------------------

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
### Testing Code
########################################################################################################################

### testing __init__() method ------------------------------------------------------------------------------------------

print("\nInit:", end=" "); my_array = Array(); print(my_array, "\n")

### testing insert() method --------------------------------------------------------------------------------------------

print("Insert():", end=" "); my_array.insert(); print(my_array)
print("Insert('error','error'):", end=" "); my_array.insert(insertIndex="error", insertValue="error")
print("Insert(-3,'error'):", end=" "); my_array.insert(insertIndex=-3, insertValue="error")
print("Insert(1,'error'):", end=" "); my_array.insert(insertIndex=1, insertValue="error")
print("Insert(0,'there'):", end=" "); my_array.insert(insertIndex=0, insertValue="there"); print(my_array)
print("Insert(0,'Hello'):", end=" "); my_array.insert(insertIndex=0, insertValue="Hello"); print(my_array)
print("Insert(2,'sweet'):", end=" "); my_array.insert(insertIndex=2, insertValue="sweet"); print(my_array, "\n")

### testing push() method ----------------------------------------------------------------------------------------------

print("Push(16):", end=" "); my_array.push(pushValue=16); print(my_array)
print("Push('?'):", end=" "); my_array.push(pushValue="?"); print(my_array, "\n")

### testing __setitem__() method ---------------------------------------------------------------------------------------

print("Set['error']='error':", end=" "); my_array["error"] = "error"
print("Set[-1]='error':", end=" "); my_array[-1] = "error"
print("Set[6]='error':", end=" "); my_array[6] = "error"
print("Set[0]='Hey':", end=" "); my_array[0] = "Hey"; print(my_array)
print("Set[3]=42:", end=" "); my_array[3] = 42; print(my_array)
print("Set[5]='!':", end=" "); my_array[5] = "!"; print(my_array, "\n")

### testing __getitem__() method ---------------------------------------------------------------------------------------

print("Get['error']:", my_array["error"])
print("Get[-1]:", my_array[-1])
print("Get[6]:", my_array[6])
print("Get[0]:", my_array[0])
print("Get[3]:", my_array[3])
print("Get[5]:", my_array[5], "\n")

### testing delete() method --------------------------------------------------------------------------------------------

print("Delete():", my_array.delete(), my_array)
print("Delete('error'):", my_array.delete(deleteIndex="error"))
print("Delete(-3):", my_array.delete(deleteIndex=-3))
print("Delete(5):", my_array.delete(deleteIndex=5))
print("Delete(0):", my_array.delete(deleteIndex=0), my_array)
print("Delete(2):", my_array.delete(deleteIndex=2), my_array)
print("Delete(2):", my_array.delete(deleteIndex=2), my_array, "\n")

### testing pop() method -----------------------------------------------------------------------------------------------

print("Pop():", my_array.pop(), my_array)
print("Pop():", my_array.pop(), my_array)
print("Pop():", my_array.pop(), my_array, "\n")
sys.exit()

print("Set[0] 'Hey':")
my_array[0] = "Hey"
print(my_array)
print("Get[0]:", my_array[0], "\n")
