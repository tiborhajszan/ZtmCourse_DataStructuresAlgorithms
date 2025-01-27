########################################################################################################################
### Data Structures and Algorithms :: Section 10
### Binary Search Tree Implementation
########################################################################################################################

### imports ------------------------------------------------------------------------------------------------------------

import sys
from typing import List, Dict, Any

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

        self.root: Dict[str,Any] = None
        self.level: int = int(0)
        self.values: List[List[Any]] = list()
        return
    
    ### traverse private method ########################################################################################
    def _traverse(self, traverseNode:Dict[str,Any]=None) -> None:
        """
        Collects all values stored in the binary search tree level-wise into lists.

        Args:
        - traverseNode : Dict[str,Any] | None, node to be collected, defaults to None
        
        Returns:
        - None
        """

        ### handling empty node > returning none -----------------------------------------------------------------------

        if traverseNode is None: return

        ### incrementing level counter ---------------------------------------------------------------------------------

        self.level += 1
        
        ### traversing tree to collect values --------------------------------------------------------------------------

        self._traverse(traverseNode=traverseNode["left"])
        self.values[self.level].append(traverseNode["value"])
        self._traverse(traverseNode=traverseNode["right"])

        ### decrementing level counter > returning none ----------------------------------------------------------------

        self.level -= 1
        return
    
    ### insert method ##################################################################################################
    def insert(self, insertValue:Any=None) -> bool:
        """
        Adds a new node containing the specified value to the binary search tree.

        Args:
        - insertValue : int | float | None, value of node to be inserted, defaults to None

        Returns:
        - bool, True = node is inserted | False = node is not inserted
        """

        ### invalid insert value > returning false ---------------------------------------------------------------------

        if insertValue is None or not isinstance(insertValue, (int, float)): return False

        ### setting initial conditions ---------------------------------------------------------------------------------

        parent_node: Dict[str,Any] = None
        insert_node: Dict[str,Any] = self.root
        new_node: Dict[str,Any] = {"left": None, "value": insertValue, "right": None}

        ### traversing tree to find insert node ------------------------------------------------------------------------

        while insert_node is not None:
            parent_node = insert_node
            insert_node = parent_node["left"] if insertValue < parent_node["value"] else parent_node["right"]
        
        ### inserting new node > returning true ------------------------------------------------------------------------

        if self.root is None: self.root = new_node
        elif insertValue < parent_node["value"]: parent_node["left"] = new_node
        else: parent_node["right"] = new_node
        return True
    
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

        ### setting initial conditions ---------------------------------------------------------------------------------

        search_node: Dict[str,Any] = self.root

        ### traversing tree to find search value > returning true if found ---------------------------------------------
        
        while search_node is not None:
            if search_node["value"] == searchValue: return True
            search_node = search_node["left"] if searchValue < search_node["value"] else search_node["right"]
        
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

print()
my_bst = BinarySearchTree()
print("Root:", my_bst.root, "\n")
print("Insert(9.6):", my_bst.insert(insertValue=9.6), "\n")
print("Root:", my_bst.root, "\n")
print("Insert(4):", my_bst.insert(insertValue=4), "\n")
print("Root:", my_bst.root, "\n")
print("Insert(20):", my_bst.insert(insertValue=20), "\n")
print("Root:", my_bst.root, "\n")
print("Insert(1):", my_bst.insert(insertValue=1), "\n")
print("Root:", my_bst.root, "\n")
print("Insert(6):", my_bst.insert(insertValue=6), "\n")
print("Root:", my_bst.root, "\n")
print("Insert(15):", my_bst.insert(insertValue=15), "\n")
print("Root:", my_bst.root, "\n")
print("Insert(170):", my_bst.insert(insertValue=170), "\n")
print("Root:", my_bst.root, "\n")
print("Insert(16):", my_bst.insert(insertValue=16), "\n")
print("Root:", my_bst.root, "\n")

### 9
### 4 20
### 1 6 15 170
### 16
