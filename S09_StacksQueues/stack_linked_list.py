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

### testing code #######################################################################################################

myStack: Stack = Stack()
print()
myStack.print()
myStack.push(pushValue=1)
myStack.print()
myStack.push(pushValue=2)
myStack.print()
myStack.push(pushValue=3)
myStack.print()
myStack.push(pushValue=4)
myStack.print()
