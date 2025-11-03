########################################################################################################################
### Data Structures and Algorithms
### Section 14 | Breadth/Depth First Search Implementations
########################################################################################################################

from typing import List, Dict, Any

########################################################################################################################
### Binary Search Tree Class
########################################################################################################################

class BinarySearchTree:
    """
    Implements a simple Binary Search Tree data structure.

    Methods:
    - __init__() : initializes Binary Search Tree object
    - _bfsIterative() : performs iterative Breadth First Search
    - _bfsRecursive() : performs recursive Breadth First Search
    - _dfsPreOrder() : performs PreOrder Depth First Search
    - _dfsInOrder() : performs InOrder Depth First Search
    - _dfsPostOrder() : performs PostOrder Depth First Search
    - _traverse() : collects all values stored in Binary Search Tree
    - __str__() : defines string representation
    - insert() : adds new node
    - __contains__() : defines "in" operator
    - delete() : removes node
    """

    ### constructor method #############################################################################################

    def __init__(self) -> None:
        """
        Initializes a new Binary Search Tree object with an empty root node.

        Args:
        - None

        Attributes:
        - empty_node : Dict[str,Any], empty node template
        - root_node : Dict[str,Any], root node of Binary Search Tree, defaults to empty node

        - level : int, level index of Binary Search Tree, defaults to 0
        - value_list : List[Any], list of Binary Search Tree values, defaults to empty list
        - recursive_list : List[Any], recursive list of Binary Search Tree values, defaults to empty list
        - values : List[List[Any]], level-wise list of Binary Search Tree values, defaults to empty list

        Returns:
        - None
        """

        self.empty_node: Dict[str,Any] = {"left": {}, "value": None, "right": {}}
        self.root_node: Dict[str,Any] = self.empty_node
        # self.level: int = int(0)
        # self.value_list: List[Any] = list()
        # self.recursive_list: List[Any] = list()
        # self.inorder_list: List[Any] = list()
        return
    
    ### linear breadth first search method #############################################################################

    def _bfsLinear(self) -> None:
        """
        Performs a linear Breadth First Search on the Binary Search Tree object.

        Args:
        - None

        Returns:
        - None
        """

        ### method init ------------------------------------------------------------------------------------------------

        self.value_list = list()
        current_node: Dict[str,Any] = self.root
        node_queue: List[Dict[str,Any]] = list()
        node_queue.append(current_node)

        ### breadth first search ---------------------------------------------------------------------------------------

        while 0 < len(node_queue):
            current_node = node_queue.pop(0)
            self.value_list.append(current_node["value"])
            if current_node["left"] is not None: node_queue.append(current_node["left"])
            if current_node["right"] is not None: node_queue.append(current_node["right"])
        
        ### method termination -----------------------------------------------------------------------------------------

        return
    
    ### recursive breadth first search method ##########################################################################

    def _bfsRecursive(self, nodeQueue:List[Dict[str,Any]], valueList:List[Any]) -> List[Any]:
        """
        Performs a recursive Breadth First Search on the Binary Search Tree.

        Args:
        - nodeQueue : List[Dict[str,Any]], queue of nodes to be searched
        - valueList : List[Any], list of Binary Search Tree values

        Returns:
        - List[Any], list of Binary Search Tree values
        """

        ### base case --------------------------------------------------------------------------------------------------

        if len(nodeQueue) == 0: return valueList

        ### method main logic ------------------------------------------------------------------------------------------

        current_node: Dict[str,Any] = nodeQueue.pop(0)
        valueList.append(current_node["value"])
        if len(current_node["left"]) != 0: nodeQueue.append(current_node["left"])
        if len(current_node["right"]) != 0: nodeQueue.append(current_node["right"])
        
        ### recursive case ---------------------------------------------------------------------------------------------

        return self._bfsRecursive(nodeQueue=nodeQueue, valueList=valueList)
    
    ### preorder depth first search private method #####################################################################

    def _dfsPreOrder(self, currentNode:Dict[str,Any], valueList:List[Any]) -> List[Any]:
        """
        Performs a PreOrder Depth First Search in the Binary Search Tree.

        Args:
        - currentNode : Dict[str,Any], current node to be processed
        - valueList : List[Any], list of Binary Search Tree values

        Returns:
        - List[Any], list of Binary Search Tree values
        """

        valueList.append(currentNode["value"])
        if len(currentNode["left"]) != 0: self._dfsPreOrder(currentNode=currentNode["left"], valueList=valueList)
        if len(currentNode["right"]) != 0: self._dfsPreOrder(currentNode=currentNode["right"], valueList=valueList)
        return valueList
    
    ### inorder depth first search private method ######################################################################

    def _dfsInOrder(self, currentNode:Dict[str,Any], valueList:List[Any]) -> List[Any]:
        """
        Performs an InOrder Depth First Search in the Binary Search Tree.

        Args:
        - currentNode : Dict[str,Any], current node to be processed
        - valueList : List[Any], list of Binary Search Tree values

        Returns:
        - List[Any], list of Binary Search Tree values
        """

        if len(currentNode["left"]) != 0: self._dfsInOrder(currentNode=currentNode["left"], valueList=valueList)
        valueList.append(currentNode["value"])
        if len(currentNode["right"]) != 0: self._dfsInOrder(currentNode=currentNode["right"], valueList=valueList)
        return valueList
    
    ### postorder depth first search private method ####################################################################

    def _dfsPostOrder(self, currentNode:Dict[str,Any], valueList:List[Any]) -> List[Any]:
        """
        Performs a PostOrder Depth First Search in the Binary Search Tree.

        Args:
        - currentNode : Dict[str,Any], current node to be processed
        - valueList : List[Any], list of Binary Search Tree values

        Returns:
        - List[Any], list of Binary Search Tree values
        """

        if len(currentNode["left"]) != 0: self._dfsPostOrder(currentNode=currentNode["left"], valueList=valueList)
        if len(currentNode["right"]) != 0: self._dfsPostOrder(currentNode=currentNode["right"], valueList=valueList)
        valueList.append(currentNode["value"])
        return valueList


    ### traverse private method ########################################################################################
    def _traverse(self, traverseNode:Dict[str,Any]) -> None:
        """
        Collects all values stored in the Binary Search Tree object into a level-wise container.

        Args:
        - traverseNode : Dict[str,Any], node to be collected
        
        Returns:
        - None
        """

        ### incrementing level counter and values list -----------------------------------------------------------------

        self.level += 1
        if len(self.values) < self.level: self.values.append(list())
        
        ### traversing tree recursively to collect values --------------------------------------------------------------

        if traverseNode["left"] is not None: self._traverse(traverseNode=traverseNode["left"])
        self.values[self.level-1].append(traverseNode["value"])
        if traverseNode["right"] is not None: self._traverse(traverseNode=traverseNode["right"])

        ### decrementing level counter > returning none ----------------------------------------------------------------

        self.level -= 1
        return
    
    ### str dunder method ##############################################################################################

    def __str__(self) -> str:
        """
        Defines string representation for the Binary Search Tree.

        Args:
        - None

        Returns:
        - str, string representation of Binary Search Tree
        """

        ### tree empty > returning empty message -----------------------------------------------------------------------

        if self.root_node["value"] is None: return "\nEmpty Tree\n"

        ### tree not empty > returning string representation -----------------------------------------------------------

        preorder_str: str = str(self._dfsPreOrder(currentNode=self.root_node, valueList=list()))
        tree_str: str = "PreOrder DFS: " + preorder_str + "\n"
        inorder_str: str = str(self._dfsInOrder(currentNode=self.root_node, valueList=list()))
        tree_str += "InOrder DFS: " + inorder_str + "\n"
        postorder_str: str = str(self._dfsPostOrder(currentNode=self.root_node, valueList=list()))
        tree_str += "PostOrder DFS: " + postorder_str + "\n"
        return tree_str
    
    ### insert method ##################################################################################################

    def insert(self, insertValue:Any=None) -> bool:
        """
        Adds a new node to the Binary Search Tree.

        Args:
        - insertValue : int | float | None, value of node to be inserted, defaults to None

        Returns:
        - bool, True = insert success | False = insert failure
        """

        ### invalid insert value > returning false ---------------------------------------------------------------------

        if insertValue is None or not isinstance(insertValue, (int, float)): return False

        ### inserting into root node > returning true ------------------------------------------------------------------

        if self.root_node["value"] is None:
            self.root_node["value"] = insertValue
            return True

        ### traversal init ---------------------------------------------------------------------------------------------

        current_node: Dict[str,Any] = self.root_node
        new_node: Dict[str,Any] = {"left": {}, "value": insertValue, "right": {}}

        ### traversal > inserting into leaf node -----------------------------------------------------------------------

        while len(current_node) != 0:

            ### going left
            if insertValue < current_node["value"]:
                if len(current_node["left"]) == 0: current_node["left"] = new_node; break
                else: current_node = current_node["left"]; continue
            
            ### going right
            else:
                if len(current_node["right"]) == 0: current_node["right"] = new_node; break
                else: current_node = current_node["right"]; continue
        
        ### returning true ---------------------------------------------------------------------------------------------

        return True
    
    ### contains dunder method #########################################################################################
    def __contains__(self, containsValue:Any) -> bool:
        """
        Defines the "in" operator for the Binary Search Tree class.

        Args:
        - containsValue : Any, value to be searched for

        Returns:
        - bool, True = value is found | False = value is not found
        """

        ### empty tree | invalid contains value > returning false ------------------------------------------------------

        if self.root is None or not isinstance(containsValue, (int, float)): return False

        ### setting initial conditions ---------------------------------------------------------------------------------

        search_node: Dict[str,Any] = self.root

        ### traversing tree to find contains value > returning true if found -------------------------------------------
        
        while search_node is not None:
            if search_node["value"] == containsValue: return True
            search_node = search_node["left"] if containsValue < search_node["value"] else search_node["right"]
        
        ### contains value not found > returning false -----------------------------------------------------------------

        return False
    
    ### delete method ##################################################################################################
    def delete(self, deleteValue:Any=None) -> bool:
        """
        Removes a node containing the specified value from the Binary Search Tree object.

        Args:
        - deleteValue : int | float | None, value of node to be deleted, defaults to None

        Returns:
        - bool, True = node is deleted | False = node is not deleted
        """

        ### empty tree | invalid delete value > returning false --------------------------------------------------------

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
print(my_bst)

print("Insert(9):", my_bst.insert(insertValue=9))
print("Insert(4):", my_bst.insert(insertValue=4))
print("Insert(20):", my_bst.insert(insertValue=20))
print("Insert(1):", my_bst.insert(insertValue=1))
print("Insert(6):", my_bst.insert(insertValue=6))
print("Insert(15):", my_bst.insert(insertValue=15))
print("Insert(170):", my_bst.insert(insertValue=170))
print("Insert(14.0):", my_bst.insert(insertValue=14.0))
print("Insert(14.1):", my_bst.insert(insertValue=14.1))
print("Insert(15.0):", my_bst.insert(insertValue=15.0))
print(my_bst)

# print("Find(6):", 6 in my_bst)
# print("Delete(6):", my_bst.delete(deleteValue=6), "\n")

# print("Insert():", my_bst.insert())
# print("Insert('9'):", my_bst.insert(insertValue='9'))
# print(my_bst)

# print("Find('6'):", '6' in my_bst)
# print("Find(6):", 6 in my_bst)
# print("Find(6.0):", 6.0 in my_bst)
# print("Find(85.02):", 85.02 in my_bst, "\n")

# print("Delete():", my_bst.delete())
# print("Delete('6'):", my_bst.delete(deleteValue='6'))
# print("Delete(85.02):", my_bst.delete(deleteValue=85.02))
# print("Delete(1):", my_bst.delete(deleteValue=1))
# print("Delete(170.0):", my_bst.delete(deleteValue=170.0))
# print(my_bst)

# print("Delete(4):", my_bst.delete(deleteValue=4))
# print("Delete(20):", my_bst.delete(deleteValue=20))
# print(my_bst)

# print("Delete(9):", my_bst.delete(deleteValue=9))
# print(my_bst)

# print("Delete(14.0):", my_bst.delete(deleteValue=14.0))
# print(my_bst)

# print("Delete(14.1):", my_bst.delete(deleteValue=14.1))
# print(my_bst)

# print("Delete(15):", my_bst.delete(deleteValue=15))
# print(my_bst)

# print("Delete(15.0):", my_bst.delete(deleteValue=15.0))
# print(my_bst)

# print("Delete(6):", my_bst.delete(deleteValue=6))
# print(my_bst)

### 9
### 4 20
### 1 6 15 170
### 14.0 15.0
### 14.1
