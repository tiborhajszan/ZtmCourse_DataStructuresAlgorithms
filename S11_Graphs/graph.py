########################################################################################################################
### Data Structures and Algorithms :: Section 11
### Graph Implementation
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
        
        ### returning string -------------------------------------------------------------------------------------------

        return graph_string

########################################################################################################################
### testing code
########################################################################################################################

print()
my_graph = Graph()
print("Init:", my_graph)
