########################################################################################################################
### Data Structures and Algorithms :: Section 09
### Queue Implementation Using Linked List
########################################################################################################################

### imports ############################################################################################################

from typing import List, Dict, Any

########################################################################################################################
### Queue Class
########################################################################################################################

class Queue:

    ### constructor method #############################################################################################
    def __init__(self) -> None:
        """
        Initializes a new empty Queue object.

        Attributes:
        - front : Dict[str,Any], first node of queue
        - end : Dict[str,Any], last node of queue
        - length : int, number of nodes in queue

        Returns:
        - None
        """

        ### initializing attributes ------------------------------------------------------------------------------------

        self.front: Dict[str,Any] = None
        self.end: Dict[str,Any] = None
        self.length: int = int(0)

        ### returning none ---------------------------------------------------------------------------------------------

        return
    
    ### empty method ###################################################################################################
    def empty(self) -> bool:
        """
        Checks if the queue is empty.

        Returns:
        - bool: True = queue is empty | False = queue is not empty
        """

        return self.length == 0
    
    ### push method ####################################################################################################
    def push(self, pushValue:Any=None) -> None:
        """
        Adds a new node to the end of the queue.

        Args:
        - pushValue : Any | None, value of new node, defaults to None
        
        Returns:
        - None
        """

        ### establishing new node sequence -----------------------------------------------------------------------------

        old_end: Dict[str,Any] = self.end
        new_end: Dict[str,Any] = {"value": pushValue, "next": None}

        ### updating pointers ------------------------------------------------------------------------------------------

        if not self.empty(): old_end["next"] = new_end

        ### updating attributes ----------------------------------------------------------------------------------------

        if self.empty(): self.front = new_end
        self.end = new_end
        self.length += 1

        ### returning none ---------------------------------------------------------------------------------------------
        
        return
    
    ### peek method ####################################################################################################
    def peek(self) -> Any:
        """
        Returns the value of the front node from the queue.

        Returns:
        - None, if queue is empty | Any, value of front node
        """

        return None if self.empty() else self.front["value"]
    
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

myQueue: Queue = Queue()
print()
print(myQueue.front, myQueue.end, myQueue.length)
# myStack.print()
print("Peek: ", myQueue.peek())
print("Empty? ", myQueue.empty(), "\n")

myQueue.push(pushValue=1)
# myStack.print()
myQueue.push(pushValue=2)
# myStack.print()
myQueue.push(pushValue=3)
print(myQueue.front, myQueue.end, myQueue.length)
# myStack.print()
print("Peek: ", myQueue.peek())
print("Empty? ", myQueue.empty(), "\n")

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
