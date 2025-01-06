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
    def __init__(self, value=None) -> None:
        """
        Args:
        - value : Any, value of head node, defaults to None

        Initializes a new LinkedList object with a single head node.

        Attributes:
        - head : Dict[str,Any], head of linked list (first node)
        - tail : Dict[str,Any], tail of linked list (last node)
        - length : int, number of nodes in linked list

        Returns:
        - None
        """

        self.head = {"value": value, "next": None}
        self.tail = self.head
        self.length = int(1)
        return

### testing code #######################################################################################################

myLiLi = LinkedList(value=10)
print()
print("Head: ", myLiLi.head, "\n")
print("Tail: ", myLiLi.tail, "\n")
print("Size: ", myLiLi.length, "\n")
