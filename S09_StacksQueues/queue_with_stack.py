########################################################################################################################
### Data Structures and Algorithms :: Section 09
### Interview Question: Queue Implementation Using Array Stack
########################################################################################################################

### imports ############################################################################################################

from typing import List, Dict, Any

########################################################################################################################
### Queue With Stack Class
########################################################################################################################

class QueueWithStack:
    """
    Interview Question:
    - Implement a queue data structure using two stacks for data storage.

    Methods to Implement:
    - empty() : checks if the queue is empty
    - push() : adds a new item to the end of the queue
    - peek() : returns the value at the front of the queue
    - pop() : removes the item from the front of the queue and returns its value
    """

    ### constructor method #############################################################################################
    def __init__(self) -> None:
        """
        Initializes a new empty QueueWithStack object.

        Attributes:
        - in_stack : List[Any], container to store incoming items
        - out_stack : List[Any], container to store outgoing items

        Returns:
        - None
        """

        self.in_stack: List[Any] = list()
        self.out_stack: List[Any] = list()
        return
    
    ### is empty method ################################################################################################
    def is_empty(self) -> bool:
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

        if len(self.array) == 0: return
        return self.array[-1]
    
    ### print method ###################################################################################################
    def print(self) -> None:
        """
        Prints all values stored in the stack from top to bottom.
        
        Returns:
        - None
        """

        print("Values: ", self.array[::-1], "\n")
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

myCraizyQueue: QueueWithStack = QueueWithStack()
print()
print(myCraizyQueue.in_stack, myCraizyQueue.out_stack, "\n")
# myStack.print()
# print("Peek: ", myStack.peek())
# print("Is Empty: ", myStack.is_empty(), "\n")

# myStack.push(pushValue=1)
# myStack.print()
# myStack.push(pushValue=2)
# myStack.print()
# myStack.push(pushValue=3)
# myStack.print()
# print("Peek: ", myStack.peek())
# print("Is Empty: ", myStack.is_empty(), "\n")

# print("Pop: ", myStack.pop())
# myStack.print()
# print("Pop: ", myStack.pop())
# myStack.print()
# print("Pop: ", myStack.pop())
# myStack.print()
# print("Pop: ", myStack.pop())
# myStack.print()
# print("Peek: ", myStack.peek())
# print("Is Empty: ", myStack.is_empty(), "\n")
