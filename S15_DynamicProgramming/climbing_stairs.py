########################################################################################################################
### Data Structures And Algorithms
### Section 15 | Dynamic Programming | Climbing Stairs
########################################################################################################################

from typing import Dict
import random

### climbing stairs function ###########################################################################################

def climbing_stairs():
    """
    Finds the solution for the Climbing Stairs coding problem:  
    https://leetcode.com/problems/climbing-stairs/description/  
    Uses recursive dynamic programming, closure, and memoization.

    ### Parameters
    - stairNum : int, number of stairs  
        1 <= stairNum <= 45  
        defaults to 0
    ### Returns
    - int, number of ways to climb the stairs
    - -1, invalid argument
    """

    ### memoization init -----------------------------------------------------------------------------------------------

    cache: Dict[int, int] = dict()

    ### defining closure -----------------------------------------------------------------------------------------------

    def closure(stairNum:int=0) -> int:

        ### invalid argument > returning -1
        if type(stairNum) is not int or stairNum < 1 or 45 < stairNum: return -1

        ### base cases > returning base options
        if stairNum < 4: return stairNum

        ### known staircase > returning cached options
        if stairNum in cache.keys(): return cache[stairNum]

        ### new staircase > returning calculated options
        cache[stairNum] = closure(stairNum-1) + closure(stairNum-2)
        return cache[stairNum]

    ### returning closure ----------------------------------------------------------------------------------------------

    return closure

########################################################################################################################
### testing code
########################################################################################################################

print()

print("Climbing Stairs")
print()

print("Stairs() =", climbing_stairs()())
print()

print(f"Stairs('test') = {climbing_stairs()(stairNum='test')}")
print(f"Stairs(-1) = {climbing_stairs()(stairNum=-1)}")
print(f"Stairs(55) = {climbing_stairs()(stairNum=55)}")
print()

print(f"Stairs(1) = {climbing_stairs()(stairNum=1)}")
print(f"Stairs(2) = {climbing_stairs()(stairNum=2)}")
print(f"Stairs(3) = {climbing_stairs()(stairNum=3)}")
print()

stair_num: int = random.randint(1, 45)
print(f"Stairs({stair_num}) = {climbing_stairs()(stairNum=stair_num)}")
print()
