########################################################################################################################
### Data Structures And Algorithms
### Section 15 | Dynamic Programming | House Robber
########################################################################################################################

from typing import List
import random

### house robber function ##############################################################################################

def house_robber(moneyList:List[int]=list()) -> int:
    """
    Finds the solution for the House Robber coding problem.  
    https://leetcode.com/problems/house-robber/description/  
    Uses iterative dynamic programming and memory optimization.

    ### Parameters:
    - moneyList : List[int], amount of money stashed at each house  
        1 <= moneyList.length <= 100, 0 <= moneyList[i] <= 400  
        defaults to empty list
    ### Returns:
    - int, maximum available loot
    - -1, invalid argument
    """

    ### invalid argument > returning -1 > ------------------------------------------------------------------------------

    if type(moneyList) is not list or len(moneyList) < 1 or 100 < len(moneyList): return -1
    if any(type(money) is not int or money < 0 or 400 < money for money in moneyList): return -1

    ### base cases > returning maximum loot ----------------------------------------------------------------------------

    if len(moneyList) == 1: return moneyList[0]
    if len(moneyList) == 2: return max(moneyList)

    ### registers init -------------------------------------------------------------------------------------------------

    previous2: int = moneyList[0]
    previous1: int = max(moneyList[0], moneyList[1])
    max_loot: int = 0
    
    ### calculating maximum loot ---------------------------------------------------------------------------------------

    for money in moneyList[2:]:
        max_loot = max(previous2 + money, previous1)
        previous2 = previous1
        previous1 = max_loot

    ### returning maximum loot -----------------------------------------------------------------------------------------

    return max_loot

########################################################################################################################
### testing code
########################################################################################################################

print()

print("House Robber")
print()

print(f"Robber() = {house_robber()}")
print()

print(f"Robber('test') = {house_robber(moneyList='test')}")
print(f"Robber([]) = {house_robber(moneyList=[])}")
print(f"Robber([1]*105) = {house_robber(moneyList=[1]*105)}")
print()

print(f"Robber([300,'test',5]) = {house_robber(moneyList=[300,'test',5])}")
print(f"Robber([300,400,-5]) = {house_robber(moneyList=[300,400,-5])}")
print(f"Robber([300,400,500]) = {house_robber(moneyList=[300,400,500])}")
print()

print(f"Robber([5]) = {house_robber(moneyList=[5])}")
print(f"Robber([1,8]) = {house_robber(moneyList=[1,8])}")
print()

money_list: List[int] = [random.randint(0, 400) for _ in range(100)]
print(f"Robber({money_list}) = {house_robber(moneyList=money_list)}")
print()
