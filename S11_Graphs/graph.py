########################################################################################################################
### Data Structures and Algorithms :: Section 11
### Graph Implementation Using Dictionary as Adjacency / Node List
########################################################################################################################

### imports ------------------------------------------------------------------------------------------------------------

from typing import Dict, Any

########################################################################################################################
### Graph Class
########################################################################################################################

class Graph:

    ### constructor method #############################################################################################
    def __init__(self):
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

        self.nodes: Dict[Any,Any] = dict()
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
    
    ### add node method ################################################################################################
    def add_node(self, nodeValue:Any=None) -> bool:
        """
        Adds a new node containing the specified value to the Graph object.

        Args:
        - nodeValue : Any | None, value of node to be added, defaults to None

        Returns:
        - bool, True = node is added | False = node is not added
        """

        ### node already exists > returning false ----------------------------------------------------------------------

        if nodeValue in self.nodes: return False

        ### adding node to graph > incrementing size > returning true --------------------------------------------------

        self.nodes[nodeValue] = list()
        self.size += 1
        return True

########################################################################################################################
### testing code
########################################################################################################################

print()
my_graph = Graph()
print("Init:")
print(my_graph)

print("Add Node 0:", my_graph.add_node(nodeValue=0))
print("Add Node 1:", my_graph.add_node(nodeValue=1))
print("Add Node 2:", my_graph.add_node(nodeValue=2))
print(my_graph)
print("Add Node 3:", my_graph.add_node(nodeValue=3))
print("Add Node 4:", my_graph.add_node(nodeValue=4))
print("Add Node 5:", my_graph.add_node(nodeValue=5))
print(my_graph)
print("Add Node 6:", my_graph.add_node(nodeValue=6))
print("Add Node ():", my_graph.add_node())
print("Add Node 3:", my_graph.add_node(nodeValue=3))
print(my_graph)
