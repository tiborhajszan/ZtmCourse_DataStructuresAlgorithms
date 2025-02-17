########################################################################################################################
### Data Structures and Algorithms :: Section 09
### Stack Implementation Using Linked List
########################################################################################################################

### imports ############################################################################################################

from typing import List, Dict, Any

########################################################################################################################
### Stack Class
########################################################################################################################

class Stack:
    """
    Implements a basic Stack data structure on top of a linked list.

    Methods:
    - __init__ : Initializes a new empty Stack object.
    - is_empty : Checks if the stack is empty.
    - push : Adds a new node to the top of the stack.
    - peek : Returns the value of the top node.
    - print : Prints all values stored in the stack from top to bottom.
    - pop : Removes the top node from the stack and returns its value.
    """

    ### constructor method #############################################################################################
    def __init__(self) -> None:
        """
        Initializes a new empty Stack object.

        Attributes:
        - top : Dict[str,Any], top node of stack
        - bottom : Dict[str,Any], bottom node of stack
        - length : int, number of nodes in stack

        Returns:
        - None
        """

        ### initializing attributes ------------------------------------------------------------------------------------

        self.top: Dict[str,Any] = None
        self.bottom: Dict[str,Any] = None
        self.length: int = int(0)

        ### returning none ---------------------------------------------------------------------------------------------

        return
    
    ### is empty method ################################################################################################
    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        Returns:
        - bool: True = stack is empty | False = stack is not empty
        """

        return self.length == 0
    
    ### push method ####################################################################################################
    def push(self, pushValue:Any=None) -> None:
        """
        Adds a new node to the top of the stack.

        Args:
        - pushValue : Any | None, value of new node, defaults to None
        
        Returns:
        - None
        """

        ### establishing new node sequence -----------------------------------------------------------------------------

        new_top: Dict[str,Any] = {"value": pushValue, "next": None}
        old_top: Dict[str,Any] = self.top

        ### updating pointers ------------------------------------------------------------------------------------------

        new_top["next"] = old_top

        ### updating attributes ----------------------------------------------------------------------------------------

        self.top = new_top
        if self.length == 0: self.bottom = new_top
        self.length += 1

        ### returning none ---------------------------------------------------------------------------------------------
        
        return
    
    ### peek method ####################################################################################################
    def peek(self) -> Any:
        """
        Returns the value of the top node.

        Returns:
        - None, if stack is empty | Any, value of top node
        """

        if self.length == 0: return
        return self.top["value"]
    
    ### print method ###################################################################################################
    def print(self) -> None:
        """
        Prints all values stored in the stack from top to bottom.
        
        Returns:
        - None
        """

        ### setting initial conditions ---------------------------------------------------------------------------------

        current_node: Dict[str,Any] = self.top
        value_list: List[Any] = list()

        ### traversing stack to collect values -------------------------------------------------------------------------

        while current_node is not None:
            value_list.append(current_node["value"])
            current_node = current_node["next"]

        ### printing values and attributes -----------------------------------------------------------------------------

        print("Values: ", value_list)
        top: Any = self.top["value"] if self.top is not None else None
        print("Top: ", top)
        bottom: Any = self.bottom["value"] if self.bottom is not None else None
        print("Bottom: ", bottom)
        print("Length: ", self.length, "\n")

        ### returning none ---------------------------------------------------------------------------------------------

        return
    
    ### pop method #####################################################################################################
    def pop(self) -> Any:
        """
        Removes the top node from the stack and returns its value.

        Returns:
        - Any, value of removed node
        """

        ### handling empty stack ---------------------------------------------------------------------------------------

        if self.length == 0: return

        ### establishing new node sequence -----------------------------------------------------------------------------

        delete_top: Dict[str,Any] = self.top
        new_top: Dict[str,Any] = delete_top["next"]

        ### updating attributes ----------------------------------------------------------------------------------------

        self.top = new_top
        if self.length <= 2: self.bottom = new_top
        self.length -= 1

        ### returning removed value ------------------------------------------------------------------------------------
        
        return delete_top["value"]

### testing code #######################################################################################################

myStack: Stack = Stack()
print()
myStack.print()
print("Peek: ", myStack.peek())
print("Is Empty: ", myStack.is_empty(), "\n")

myStack.push(pushValue=1)
myStack.print()
myStack.push(pushValue=2)
myStack.print()
myStack.push(pushValue=3)
myStack.print()
print("Peek: ", myStack.peek())
print("Is Empty: ", myStack.is_empty(), "\n")

print("Pop: ", myStack.pop())
myStack.print()
print("Pop: ", myStack.pop())
myStack.print()
print("Pop: ", myStack.pop())
myStack.print()
print("Pop: ", myStack.pop())
myStack.print()
print("Peek: ", myStack.peek())
print("Is Empty: ", myStack.is_empty(), "\n")
