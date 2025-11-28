########################################################################################################################
### Data Structures And Algorithms
### Section 15 | Dynamic Programming | House Robber
########################################################################################################################

from typing import List
import random

### house robber function ##############################################################################################

def house_robber(plunderList:List[int]=list()) -> int:
    """
    Finds the optimized solution for the House Robber coding problem.

    Args:
    - plunderList : List[int], list of plunder values, defaults to empty list
    Returns:
    - int, maximum plunder value
    """

    ### invalid argument > returning -1 > ------------------------------------------------------------------------------

    if type(plunderList) is not list or len(plunderList) < 1 or 100 < len(plunderList): return -1
    if any(type(plunder) is not int or plunder < 0 or 400 < plunder for plunder in plunderList): return -1

    ### base cases > returning maximum plunder value -------------------------------------------------------------------

    if len(plunderList) == 1: return plunderList[0]
    if len(plunderList) == 2: return max(plunderList)

    ### calculating profit sequence ------------------------------------------------------------------------------------

    profit_sequence: List[int] = list()
    profit_sequence.append(plunderList[0])
    profit_sequence.append(max(plunderList[0], plunderList[1]))
    for house in range(2, len(plunderList)):
        profit_sequence.append(max(profit_sequence[house-1], profit_sequence[house-2]+plunderList[house]))

    ### returning maximum plunder value --------------------------------------------------------------------------------

    return profit_sequence.pop()

########################################################################################################################
### testing code
########################################################################################################################

print()

print("House Robber")
print()

print("Robber() =", house_robber())
print()

print("Robber('test') =", house_robber(plunderList="test"))
print("Robber([]) =", house_robber(plunderList=[]))
print("Robber([1]*105) =", house_robber(plunderList=[1]*105))
print()

print("Robber([300,'test',5]) =", house_robber(plunderList=[300,'test',5]))
print("Robber([300,400,-5]) =", house_robber(plunderList=[300,400,-5]))
print("Robber([300,400,500]) =", house_robber(plunderList=[300,400,500]))
print()

print("Robber([5]) =", house_robber(plunderList=[5]))
print("Robber([1,5]) =", house_robber(plunderList=[1,5]))
print()

plunder_list: List[int] = list()
for _ in range(5): plunder_list.append(random.randint(0, 401))
print(f"Robber({plunder_list}) =", house_robber(plunderList=plunder_list))
print()
