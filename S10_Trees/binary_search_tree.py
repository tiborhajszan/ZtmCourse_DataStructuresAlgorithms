########################################################################################################################
### Data Structures and Algorithms :: Section 10
### Binary Search Tree Implementation
########################################################################################################################

### imports ------------------------------------------------------------------------------------------------------------

import sys
from typing import Dict, Any

########################################################################################################################
### Binary Search Tree Class
########################################################################################################################

class BinarySearchTree:

    ### constructor method #############################################################################################
    def __init__(self) -> None:
        """
        Initializes a new Binary Search Tree object with an empty root node.

        Args:
        - None

        Attributes:
        - root : Dict[str,Any], root of binary search tree (first node), defaults to None

        Returns:
        - None
        """

        self.root = None
        return
    
    ### print method ###################################################################################################
    def print(self, printNode:Dict[str,Any]=None) -> None:
        """
        Prints all values stored in the binary search tree.

        Args:
        - printNode : Dict[str,Any] | None, node to be printed, defaults to None
        
        Returns:
        - None
        """

        ### handling empty node > returning none -----------------------------------------------------------------------

        if printNode is None: return

        ### verifying printNode argument -------------------------------------------------------------------------------

        if type(printNode) is not dict or not all(key in ["left", "value", "right"] for key in printNode.keys()):
            sys.exit("Cannot print: Invalid node...\n")
        
        ### recursive printing of nodes > returning none ---------------------------------------------------------------

        self.print(printNode["left"])
        print(printNode["value"], end=" ")
        self.print(printNode["right"])
        return
    
    ### insert method ##################################################################################################
    def insert(self, insertValue:Any=None) -> None:
        """
        Adds a new numeric node to the binary search tree.

        Args:
        - insertValue : int | float | None, value of new node, defaults to None

        Returns:
        - None
        """

        ### invalid insert value > error message -----------------------------------------------------------------------

        if insertValue is None or not isinstance(insertValue, (int, float)):
            sys.exit("Cannot insert: Invalid value...\n")

        ### creating new node ------------------------------------------------------------------------------------------

        new_node: Dict[str,Any] = {"left": None, "value": insertValue, "right": None}

        ### inserting root > returning none ----------------------------------------------------------------------------

        if self.root is None: self.root = new_node; return

        ### traversing tree to insert ----------------------------------------------------------------------------------

        current_node: Dict[str,Any] = self.root
        while True:
            ### inserting left > returning none
            if current_node["left"] is None and insertValue < current_node["value"]:
                current_node["left"] = new_node; return
            ### inserting right > returning none
            if current_node["right"] is None and current_node["value"] <= insertValue:
                current_node["right"] = new_node; return
            ### traversing to next node
            current_node = current_node["left"] if insertValue < current_node["value"] else current_node["right"]
    
    ### lookup method ##################################################################################################
    def lookup(self, lookupValue:Any=None) -> bool:
        """
        Searches the binary search tree for the specified value.

        Args:
        - lookupValue : int | float | None, value to be searched, defaults to None

        Returns:
        - bool, True = value is found | False = value is not found
        """

        ### invalid lookup value > error message -----------------------------------------------------------------------

        if lookupValue is None or not isinstance(lookupValue, (int, float)):
            sys.exit("Cannot search: Invalid lookup value...\n")

        ### empty tree > returning false -------------------------------------------------------------------------------

        if self.root is None: return False

        ### searching tree for value > returning true if found ---------------------------------------------------------
        
        current_node: Dict[str,Any] = self.root
        while current_node is not None:
            if current_node["value"] == lookupValue: return True
            current_node = current_node["left"] if lookupValue < current_node["value"] else current_node["right"]
        
        ### value not found > returning false --------------------------------------------------------------------------

        return False
    
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

### testing code #######################################################################################################

my_bst = BinarySearchTree()
print()
my_bst.print(printNode=my_bst.root)
print("15:", my_bst.lookup(lookupValue=15), "\n")
my_bst.insert(insertValue=9)
my_bst.insert(insertValue=4)
my_bst.insert(insertValue=20)
my_bst.insert(insertValue=1)
my_bst.insert(insertValue=6)
my_bst.insert(insertValue=15)
my_bst.insert(insertValue=170)
my_bst.print(printNode=my_bst.root)
print("\n")
print("15:", my_bst.lookup(lookupValue=15), "\n")
