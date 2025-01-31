########################################################################################################################
### Data Structures and Algorithms :: Section 11
### Graph Implementation Using Dictionary as Node List
########################################################################################################################

### imports ------------------------------------------------------------------------------------------------------------

from typing import List, Dict, Any

########################################################################################################################
### Graph Class
########################################################################################################################

class Graph:
    """
    Implements a simple graph data structure using a dictionary for storing the node list.

    Methods:
    - __init__() : initializes a new Graph object
    - __str__() : defines string representation for the class
    - insert_node() : adds a new node to the graph
    - insert_edge() : adds a new edge between nodes in the graph
    - delete_node() : removes a node from the graph
    """

    ### constructor method #############################################################################################
    def __init__(self) -> None:
        """
        Initializes a new empty Graph object.

        Args:
        - None

        Attributes:
        - nodes : Dict[Any,Any], adjacency / node list
        - size : int, number of nodes in graph

        Returns:
        - None
        """

        self.nodes: Dict[Any,List[Any]] = dict()
        self.size: int = int(0)
        return
    
    ### str dunder method ##############################################################################################
    def __str__(self) -> str:
        """
        Defines the string representation for the Graph class.

        Args:
        - None

        Returns:
        - graph_string : str, string representation
        """

        ### initializing return string ---------------------------------------------------------------------------------

        graph_string: str = str()

        ### empty graph > constructing empty graph message -------------------------------------------------------------

        if self.size == 0: graph_string = "Empty Graph" + "\n"

        ### graph not empty > constructing string representation of graph ----------------------------------------------

        else:
            for key,value in self.nodes.items():
                graph_string += f"{key} -> {value}\n"
            graph_string += f"Size: {self.size}\n"
        
        ### returning string -------------------------------------------------------------------------------------------

        return graph_string
    
    ### insert node method #############################################################################################
    def insert_node(self, insertValue:Any=None) -> bool:
        """
        Adds a new node containing the specified value to the Graph object.

        Args:
        - insertValue : Any | None, value of node to be added, defaults to None

        Returns:
        - bool, True = node is added | False = node is not added
        """

        ### node already exists > returning false ----------------------------------------------------------------------

        if insertValue in self.nodes.keys(): return False

        ### adding node to graph > incrementing size > returning true --------------------------------------------------

        self.nodes[insertValue] = list()
        self.size += 1
        return True
    
    ### insert edge method #############################################################################################
    def insert_edge(self, edgeNode1:Any, edgeNode2:Any) -> bool:
        """
        Adds a new edge between specified nodes to the Graph object.

        Args:
        - edgeNode1 : Any, value of first node in edge
        - edgeNode2 : Any, value of second node in edge

        Returns:
        - bool, True = edge is added | False = edge is not added
        """

        ### nonexistent nodes > returning false ------------------------------------------------------------------------

        if edgeNode1 not in self.nodes.keys() or edgeNode2 not in self.nodes.keys(): return False

        ### edge already exists > returning false ----------------------------------------------------------------------

        if edgeNode1 in self.nodes[edgeNode2]: return False

        ### adding edge to graph > returning true ----------------------------------------------------------------------

        self.nodes[edgeNode1].append(edgeNode2)
        self.nodes[edgeNode2].append(edgeNode1)
        return True
    
    ### delete node method #############################################################################################
    def delete_node(self, deleteValue:Any=None) -> bool:
        """
        Removes the node containing the specified value from the Graph object.

        Args:
        - deleteValue : Any | None, value of node to be deleted, defaults to None

        Returns:
        - bool, True = node is deleted | False = node is not deleted
        """

        ### nonexistent node > returning false -------------------------------------------------------------------------

        if deleteValue not in self.nodes.keys(): return False

        ### deleting edges ---------------------------------------------------------------------------------------------

        for node in self.nodes[deleteValue]:
            if deleteValue in self.nodes[node]: self.nodes[node].remove(deleteValue)

        ### deleting node from graph > decrementing size > returning true ----------------------------------------------

        del self.nodes[deleteValue]
        self.size -= 1
        return True

########################################################################################################################
### testing code
########################################################################################################################

print()
my_graph = Graph()
print("Init:")
print(my_graph)

print("Add Node 0:", my_graph.insert_node(insertValue=0))
print("Add Node 1:", my_graph.insert_node(insertValue=1))
print("Add Node 2:", my_graph.insert_node(insertValue=2))
print("Add Node 3:", my_graph.insert_node(insertValue=3))
print("Add Node 4:", my_graph.insert_node(insertValue=4))
print("Add Node 5:", my_graph.insert_node(insertValue=5))
print(my_graph)
print("Add Node 6:", my_graph.insert_node(insertValue=6))
print("Add Node ():", my_graph.insert_node())
print("Add Node 3:", my_graph.insert_node(insertValue=3))
print(my_graph)

print("Add Edge 3-1:", my_graph.insert_edge(edgeNode1=3, edgeNode2=1))
print("Add Edge 3-4:", my_graph.insert_edge(edgeNode1=3, edgeNode2=4))
print("Add Edge 4-2:", my_graph.insert_edge(edgeNode1=4, edgeNode2=2))
print("Add Edge 4-5:", my_graph.insert_edge(edgeNode1=4, edgeNode2=5))
print("Add Edge 1-2:", my_graph.insert_edge(edgeNode1=1, edgeNode2=2))
print("Add Edge 1-0:", my_graph.insert_edge(edgeNode1=1, edgeNode2=0))
print("Add Edge 0-2:", my_graph.insert_edge(edgeNode1=0, edgeNode2=2))
print("Add Edge 6-5:", my_graph.insert_edge(edgeNode1=6, edgeNode2=5))
print("Add Edge 5-6:", my_graph.insert_edge(edgeNode1=5, edgeNode2=6))
print("Add Edge 'xyz'-6:", my_graph.insert_edge(edgeNode1="xyz", edgeNode2=6))
print("Add Edge 6-20:", my_graph.insert_edge(edgeNode1=6, edgeNode2=20))
print(my_graph)

print("Delete Node ():", my_graph.delete_node())
print("Delete Node 20:", my_graph.delete_node(deleteValue=20))
print("Delete Node 2:", my_graph.delete_node(deleteValue=2))
print(my_graph)
