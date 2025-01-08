########################################################################################################################
### Data Structures and Algorithms :: Section 08
### Doubly Linked List Implementation
########################################################################################################################

### imports ############################################################################################################

import sys
from typing import Dict, Any

########################################################################################################################
### Doubly Linked List Class
########################################################################################################################

class DoublyLinkedList:

    ### constructor method #############################################################################################
    def __init__(self, headValue:Any=None) -> None:
        """
        Initializes a new Doubly Linked List object with a single node.

        Args:
        - headValue : Any | None, value of single node, defaults to None

        Attributes:
        - head : Dict[str,Any], head of doubly linked list (first node)
        - tail : Dict[str,Any], tail of doubly linked list (last node)
        - length : int, number of nodes in doubly linked list

        Returns:
        - None
        """

        ### initializing attributes ------------------------------------------------------------------------------------

        self.head = {"value": headValue, "prev": None, "next": None}
        self.tail = self.head
        self.length = int(1)

        ### returning none ---------------------------------------------------------------------------------------------

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
    
    ### prepend method #################################################################################################
    def prepend(self, prependValue=None) -> None:
        """
        Args:
        - prependValue : Any, value of new node, defaults to None

        Adds a new node to the beginning of the linked list.
        
        Returns:
        - None
        """

        new_node = {"value": prependValue, "next": self.head}
        self.head = new_node
        self.length += 1
        return
    
    ### traverse private method ########################################################################################
    def _traverse(self, traverseIndex:int) -> Dict[str,Any]:
        """
        Traverses the linked list to find the node at the specified index.

        Args:
        - traverseIndex : int, index of node to be returned

        Returns:
        - current_node : Dict[str,Any], node at specified index
        """

        ### setting initial conditions ---------------------------------------------------------------------------------

        counter = int(0)
        current_node = self.head

        ### traversing linked list -------------------------------------------------------------------------------------
        
        while counter < traverseIndex:
            current_node = current_node["next"]
            counter += 1
        
        ### returning current node -------------------------------------------------------------------------------------

        return current_node
    
    ### insert method ##################################################################################################
    def insert(self, insertIndex:int=None, insertValue:Any=None) -> None:
        """
        Adds a new node to the linked list at the specified index.

        Args:
        - insertIndex : int | None, index of new node, defaults to None
        - insertValue : Any | None, value of new node, defaults to None

        Returns:
        - None
        """

        ### handling edge cases ----------------------------------------------------------------------------------------

        if type(insertIndex) is not int or self.length <= insertIndex:
            self.append(appendValue=insertValue)
            return
        if insertIndex <= 0:
            self.prepend(prependValue=insertValue)
            return

        ### establishing new node sequence -----------------------------------------------------------------------------

        previous_node = self._traverse(traverseIndex=insertIndex-1)
        new_node = {"value": insertValue, "next": None}
        next_node = previous_node["next"]

        ### updating pointers and length -------------------------------------------------------------------------------

        previous_node["next"] = new_node
        new_node["next"] = next_node
        self.length += 1

        ### returning none ---------------------------------------------------------------------------------------------

        return
    
    ### delete method ##################################################################################################
    def delete(self, deleteIndex:int=None) -> None:
        """
        Removes a node from the linked list at the specified index.

        Args:
        - deleteIndex : int | None, index of node to be deleted, defaults to None

        Raises:
        - Error, Cannot delete: Invalid index...
        - Error, Cannot delete: The list contains only one node...

        Returns:
        - None
        """

        ### validating index -------------------------------------------------------------------------------------------

        if type(deleteIndex) is not int or deleteIndex < 0 or self.length <= deleteIndex:
            sys.exit("Cannot delete: Invalid index...\n")

        ### handling single node list ----------------------------------------------------------------------------------

        if self.length == 1:
            sys.exit("Cannot delete: The list contains only one node...\n")

        ### removing head node -----------------------------------------------------------------------------------------

        if deleteIndex == 0:
            self.head = self.head["next"]
            if self.length == 2: self.tail = self.head
            self.length -= 1

        ### removing tail node -----------------------------------------------------------------------------------------

        elif deleteIndex == self.length - 1:
            new_tail = self._traverse(traverseIndex=deleteIndex-1)
            new_tail["next"] = None
            self.tail = new_tail
            if self.length == 2: self.head = self.tail
            self.length -= 1

        ### removing middle node ---------------------------------------------------------------------------------------

        else:
            previous_node = self._traverse(traverseIndex=deleteIndex-1)
            delete_node = previous_node["next"]
            next_node = delete_node["next"]
            previous_node["next"] = next_node
            self.length -= 1

        ### returning none ---------------------------------------------------------------------------------------------

        return

    ### print method ###################################################################################################
    def print(self) -> None:
        """
        Prints all values stored in the doubly linked list.
        
        Returns:
        - None
        """
        
        ### setting initial conditions ---------------------------------------------------------------------------------

        current_node = self.head
        value_list = list()

        ### traversing linked list -------------------------------------------------------------------------------------

        while current_node is not None:
            value_list.append(current_node["value"])
            current_node = current_node["next"]
        
        ### printing values and list size ------------------------------------------------------------------------------

        print("Values: ", value_list)
        print("Size: ", self.length, "\n")

        ### returning none ---------------------------------------------------------------------------------------------
        
        return

### testing code #######################################################################################################

myLiLi = DoublyLinkedList(headValue=10)
print()
myLiLi.print()
# myLiLi.append(appendValue=5)
# myLiLi.append(appendValue=16)
# myLiLi.prepend(prependValue=1)
# print()
# myLiLi.print()
# myLiLi.insert(insertIndex=2, insertValue=23)
# print("Insert(2,23): ", "\n")
# myLiLi.print()
# myLiLi.delete(deleteIndex=2)
# print("Delete(2): ", "\n")
# myLiLi.print()
