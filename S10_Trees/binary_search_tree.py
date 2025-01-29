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

        ### incrementing level counter and values list -----------------------------------------------------------------

        self.level += 1
        if len(self.values) < self.level: self.values.append(list())
        
        ### traversing tree to collect values --------------------------------------------------------------------------

        self._traverse(traverseNode=traverseNode["left"])
        self.values[self.level-1].append(traverseNode["value"])
        self._traverse(traverseNode=traverseNode["right"])

        ### decrementing level counter > returning none ----------------------------------------------------------------

        self.level -= 1
        return
    
    ### str dunder method ##############################################################################################
    def __str__(self) -> str:
        """
        Returns a string representation of the binary search tree.

        Args:
        - None

        Returns:
        - str, string representation of binary search tree
        """

        ### empty tree > returning empty message -----------------------------------------------------------------------

        if self.root is None: return "Empty Tree" + "\n"

        ### tree not empty > returning string representation of tree ---------------------------------------------------

        self.level, self.values = int(0), list()
        self._traverse(traverseNode=self.root)
        return "\n".join(" ".join(str(value) for value in level) for level in self.values) + "\n"
    
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
    
    ### search private method ##########################################################################################
    def _search(self, searchValue:Any) -> bool:
        """
        Searches the binary search tree for a node containing the specified value.

        Args:
        - searchValue : int | float, value to be searched for

        Returns:
        - bool, True = value is found | False = value is not found
        """

        ### invalid search value | empty tree > returning false --------------------------------------------------------

        if self.root is None or not isinstance(searchValue, (int, float)): return False

        ### setting initial conditions ---------------------------------------------------------------------------------

        search_node: Dict[str,Any] = self.root

        ### traversing tree to find search value > returning true if found ---------------------------------------------
        
        while search_node is not None:
            if search_node["value"] == searchValue: return True
            search_node = search_node["left"] if searchValue < search_node["value"] else search_node["right"]
        
        ### search value not found > returning false -------------------------------------------------------------------

        return False
    
    ### contains dunder method #########################################################################################
    def __contains__(self, containsValue:Any) -> bool:
        """
        Defines the "in" operator for the binary search tree.

        Args:
        - containsValue : Any, value to be searched for

        Returns:
        - bool, True = value is found | False = value is not found
        """

        return self._search(searchValue=containsValue)
    
    ### delete method ##################################################################################################
    def delete(self, deleteValue:Any=None) -> bool:
        """
        Removes a node containing the specified value from the binary search tree.

        Args:
        - deleteValue : int | float | None, value of node to be deleted, defaults to None

        Returns:
        - bool, True = node is deleted | False = node is not deleted
        """

        ### invalid delete value | empty tree > returning false --------------------------------------------------------

        if self.root is None or deleteValue is None or not isinstance(deleteValue, (int, float)): return False

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
print()
print(my_bst)
print("Find(6):", 6 in my_bst)
print("Delete(6):", my_bst.delete(deleteValue=6), "\n")

print("Insert():", my_bst.insert())
print("Insert('9'):", my_bst.insert(insertValue='9'))
print("Insert(9):", my_bst.insert(insertValue=9))
print(my_bst)

print("Insert(4):", my_bst.insert(insertValue=4))
print("Insert(20):", my_bst.insert(insertValue=20))
print(my_bst)

print("Insert(1):", my_bst.insert(insertValue=1))
print("Insert(6):", my_bst.insert(insertValue=6))
print("Insert(15):", my_bst.insert(insertValue=15))
print("Insert(170):", my_bst.insert(insertValue=170))
print(my_bst)

print("Insert(14.0):", my_bst.insert(insertValue=14.0))
print("Insert(14.1):", my_bst.insert(insertValue=14.1))
print("Insert(15.0):", my_bst.insert(insertValue=15.0))
print(my_bst.root)
print(my_bst)

print("Find('6'):", '6' in my_bst)
print("Find(6):", 6 in my_bst)
print("Find(6.0):", 6.0 in my_bst)
print("Find(85.02):", 85.02 in my_bst, "\n")

print("Delete():", my_bst.delete())
print("Delete('6'):", my_bst.delete(deleteValue='6'))
print("Delete(85.02):", my_bst.delete(deleteValue=85.02))
print("Delete(1):", my_bst.delete(deleteValue=1))
print("Delete(170.0):", my_bst.delete(deleteValue=170.0))
print(my_bst)

print("Delete(4):", my_bst.delete(deleteValue=4))
print("Delete(20):", my_bst.delete(deleteValue=20))
print(my_bst)

print("Delete(9):", my_bst.delete(deleteValue=9))
print(my_bst)

print("Delete(14.0):", my_bst.delete(deleteValue=14.0))
print(my_bst)

print("Delete(14.1):", my_bst.delete(deleteValue=14.1))
print(my_bst)

print("Delete(15):", my_bst.delete(deleteValue=15))
print(my_bst)

print("Delete(15.0):", my_bst.delete(deleteValue=15.0))
print(my_bst)

print("Delete(6):", my_bst.delete(deleteValue=6))
print(my_bst)

### 9
### 4 20
### 1 6 15 170
### 14.0 15.0
### 14.1
