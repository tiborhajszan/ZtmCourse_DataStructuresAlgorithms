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
    
    ### search method ##################################################################################################
    def search(self, searchValue:Any=None) -> bool:
        """
        Searches the binary search tree for a node containing the specified value.

        Args:
        - searchValue : int | float | None, value to be searched, defaults to None

        Returns:
        - bool, True = value is found | False = value is not found
        """

        ### invalid search value | empty tree > returning false --------------------------------------------------------

        if searchValue is None or not isinstance(searchValue, (int, float)) or self.root is None: return False

        ### traversing tree to find search value > returning true if found ---------------------------------------------
        
        current_node: Dict[str,Any] = self.root
        while current_node is not None:
            if current_node["value"] == searchValue: return True
            current_node = current_node["left"] if searchValue < current_node["value"] else current_node["right"]
        
        ### search value not found > returning false -------------------------------------------------------------------

        return False
    
    ### delete method ##################################################################################################
    def delete(self, deleteValue:Any=None) -> bool:
        """
        Removes a node containing the specified value from the binary search tree.

        Args:
        - deleteValue : int | float | None, value of node to be deleted, defaults to None

        Returns:
        - bool, True = node is deleted | False = node is not found
        """

        ### invalid delete value | empty tree > returning false --------------------------------------------------------

        if deleteValue is None or not isinstance(deleteValue, (int, float)) or self.root is None: return False

        ### setting initial conditions ---------------------------------------------------------------------------------

        parent_node: Dict[str,Any] = None
        delete_node: Dict[str,Any] = self.root
        successor_node: Dict[str,Any] = None

        ### traversing tree to find delete node ------------------------------------------------------------------------

        while delete_node is not None:
            if delete_node["value"] == deleteValue: break
            parent_node = delete_node
            delete_node = delete_node["left"] if deleteValue < delete_node["value"] else delete_node["right"]

        ### delete node not found > returning false --------------------------------------------------------------------

        if delete_node is None: return False

        ### removing leaf node -----------------------------------------------------------------------------------------

        if delete_node["left"] is None and delete_node["right"] is None:
            if parent_node is None: self.root = None
            elif parent_node["left"] == delete_node: parent_node["left"] = None
            else: parent_node["right"] = None

        ### removing single-child node ---------------------------------------------------------------------------------

        elif delete_node["left"] is None or delete_node["right"] is None:
            successor_node = delete_node["left"] if delete_node["right"] is None else delete_node["right"]
            if parent_node is None: self.root = successor_node
            elif parent_node["left"] == delete_node: parent_node["left"] = successor_node
            else: parent_node["right"] = successor_node

        ### removing two-children node ---------------------------------------------------------------------------------

        else:
            parent_node = delete_node
            successor_node = delete_node["right"]
            while successor_node["left"] is not None:
                parent_node = successor_node
                successor_node = successor_node["left"]
            delete_node["value"] = successor_node["value"]
            if parent_node["right"] == successor_node: parent_node["right"] = successor_node["right"]
            else: parent_node["left"] = successor_node["right"]

        ### returning true ---------------------------------------------------------------------------------------------

        return True

########################################################################################################################
### testing code
########################################################################################################################

my_bst = BinarySearchTree()
print(); my_bst.print(printNode=my_bst.root)
print("Find 15:", my_bst.lookup(lookupValue=15), "\n")
print("Delete 15:", my_bst.delete(deleteValue=15), "\n")
my_bst.insert(insertValue=9)
my_bst.insert(insertValue=4)
my_bst.insert(insertValue=20)
my_bst.insert(insertValue=1)
my_bst.insert(insertValue=6)
my_bst.insert(insertValue=15)
my_bst.insert(insertValue=170)
my_bst.insert(insertValue=16)
# my_bst.insert(insertValue=5)
my_bst.print(printNode=my_bst.root); print("\n")
print("Find 15:", my_bst.lookup(lookupValue=15), "\n")
print("Delete 9:", my_bst.delete(deleteValue=9), "\n")
# print("Delete 15:", my_bst.delete(deleteValue=15), "\n")
my_bst.print(printNode=my_bst.root); print("\n")
