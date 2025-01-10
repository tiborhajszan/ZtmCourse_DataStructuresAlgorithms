########################################################################################################################
### Data Structures and Algorithms :: Section 09
### Stack Implementation Using Array
########################################################################################################################

### imports ############################################################################################################

from typing import List, Any

########################################################################################################################
### Stack Class
########################################################################################################################

class Stack:
    """
    Implements a basic stack data structure using an array to store data.

    Attributes:
    - array : List[Any], container to store stack data

    Methods:
    - __init__ : initializes a new empty Stack object
    - empty : checks if the stack is empty
    - push : adds a new item to the top of the stack
    - peek : returns the value of the top item
    - print : prints all values stored in the stack from bottom to top
    - pop : removes the top item from the stack and returns its value
    """

    ### constructor method #############################################################################################
    def __init__(self) -> None:
        """
        Initializes a new empty Stack object.

        Returns:
        - None
        """

        self.array: List[Any] = list()
        return
    
    ### empty method ###################################################################################################
    def empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
        - bool: True = stack is empty | False = stack is not empty
        """

        return len(self.array) == 0
    
    ### push method ####################################################################################################
    def push(self, pushValue:Any=None) -> None:
        """
        Adds a new item to the top of the stack.

        Args:
        - pushValue : Any | None, value of new item, defaults to None
        
        Returns:
        - None
        """
        
        self.array.append(pushValue)
        return
    
    ### peek method ####################################################################################################
    def peek(self) -> Any:
        """
        Returns the value of the top item.

        Returns:
        - None, if stack is empty | Any, value of top item
        """

        return None if self.empty() else self.array[-1]
    
    ### print method ###################################################################################################
    def print(self) -> None:
        """
        Prints all values stored in the stack from bottom to top.
        
        Returns:
        - None
        """

        print("Values: ", self.array, "\n")
        return
    
    ### pop method #####################################################################################################
    def pop(self) -> Any:
        """
        Removes the top item from the stack and returns its value.

        Returns:
        - None, if stack is empty | Any, value of removed item
        """

        return None if self.empty() else self.array.pop()

########################################################################################################################
### testing code
########################################################################################################################

myStack: Stack = Stack()
print()
myStack.print()
print("Peek: ", myStack.peek())
print("Empty? ", myStack.empty(), "\n")

myStack.push(pushValue=1)
myStack.print()
myStack.push(pushValue=2)
myStack.print()
myStack.push(pushValue=3)
myStack.print()
print("Peek: ", myStack.peek())
print("Empty? ", myStack.empty(), "\n")

print("Pop: ", myStack.pop())
myStack.print()
print("Pop: ", myStack.pop())
myStack.print()
print("Pop: ", myStack.pop())
myStack.print()
print("Pop: ", myStack.pop())
myStack.print()
print("Peek: ", myStack.peek())
print("Empty? ", myStack.empty(), "\n")
