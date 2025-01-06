########################################################################################################################
### Data Structures and Algorithms :: Section 08
### Linked List Implementation
########################################################################################################################

### imports ############################################################################################################

###

########################################################################################################################
### Solution
########################################################################################################################

class LinkedList:

    ### constructor method #############################################################################################
    def __init__(self, headValue=None) -> None:
        """
        Args:
        - headValue : Any, value of head node, defaults to None

        Initializes a new LinkedList object with a single head node.

        Attributes:
        - head : Dict[str,Any], head of linked list (first node)
        - tail : Dict[str,Any], tail of linked list (last node)
        - length : int, number of nodes in linked list

        Returns:
        - None
        """

        self.head = {"value": headValue, "next": None}
        self.tail = self.head
        self.length = int(1)
        return
    
    ### append method ##################################################################################################
    def append(self, appendValue=None) -> None:
        """
        Args:
        - appendValue : Any, value of new node, defaults to None

        Adds a new node to the end of the linked list.
        
        Returns:
        - None
        """

        new_node = {"value": appendValue, "next": None}
        self.tail["next"] = new_node
        self.tail = new_node
        self.length += 1
        return

### testing code #######################################################################################################

myLiLi = LinkedList(headValue=10)
myLiLi.append(appendValue=5)
myLiLi.append(appendValue=16)
print()
print("Head: ", myLiLi.head, "\n")
print("Tail: ", myLiLi.tail, "\n")
print("Size: ", myLiLi.length, "\n")
