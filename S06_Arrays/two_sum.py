########################################################################################################################
### Data Structures and Algorithms :: Section 06
### Interview Questions: Arrays :: Two Sum
########################################################################################################################

### imports
from typing import List, Dict
from random import randint

### function for creating target #######################################################################################
def create_target():
    """
    Generates a random integer between -1e+09 and 1e+09 inclusive.

    Returns:
        int, target sum
    """

    return randint(a=-1e+09, b=1e+09)

### function for creating nums array ###################################################################################
def create_nums(target=int()):
    """
    Generates an array of 10,000 random integers between -1e+09 and 1e+09 inclusive.
    Ensures that two (and only two) integers in the array add up to the target sum:
    - Generates a pair of integers that add up to the target sum;
    - Generates and prints indexes where the target integers will be placed within the nums array;
    - Creates the empty nums array and its index counter;
    - Loops until the nums array contains 10,000 integers:
        - Adds the target integers to nums array at the appropriate positions;
        - Adds random integers elsewhere that do not match the target integers;
    - Returns the nums array.

    Args:
        target: int, target sum, defaults to 0

    Returns:
        nums: List[int], list of 10,000 random integers
    """

    ### function init --------------------------------------------------------------------------------------------------

    pair_1 = randint(a=-1e+09, b=1e+09); pair_2 = target - pair_1
    index_p1 = randint(a=0, b=1e+04-1); index_p2 = randint(a=0, b=1e+04-1)
    if index_p1 == index_p2: index_p1 = index_p1 - 1 if 0 < index_p1 else index_p1 + 1
    print(index_p1, index_p2, "\n")
    nums: List[int] = list(); index_nums = int()

    ### generating nums array ------------------------------------------------------------------------------------------

    while len(nums) < 1e+04:
        if index_nums == index_p1: nums.append(pair_1)
        elif index_nums == index_p2: nums.append(pair_2)
        else:
            num = randint(a=-1e+09, b=1e+09)
            if num == pair_1 or num == pair_2: continue
            nums.append(num)
        index_nums += 1
    
    ### returning nums array -------------------------------------------------------------------------------------------

    return nums

### solution function ##################################################################################################
def two_sum(nums: List[int]=[], target=int()):
    """
    Interview Question:
    Given an array of integers "nums" and an integer "target", return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

    This solution uses linear complement search within a hash table:
    - Loops through indexes of the input array;:
        - Computes the complement of current integer from input array;
        - Returns index of complement and index of current integer if complement exists in hash table;
        - Adds current integer and its index to hash table if complement does not exist in hash table;
    - Returns empty list if no solution is found.

    Args:
    - nums: List[int], list of unsorted integers, defaults to empty list
    - target: int, target sum, defaults to 0

    Returns:
    - List[int], indices of two integers in input array that add up to target sum
    """

    ### function init --------------------------------------------------------------------------------------------------

    complement = int()
    numsHash: Dict[int,int] = dict()

    ### search loop > solution found > returning indices ---------------------------------------------------------------

    for index in range(len(nums)):
        complement = target - nums[index]
        if complement in numsHash: return [numsHash[complement], index]
        numsHash[nums[index]] = index

    ### no solution found > returning empty list -----------------------------------------------------------------------

    return []

### testing ############################################################################################################

print()
currentTarget = create_target()
currentNums = create_nums(target=currentTarget)
solution = two_sum(nums=currentNums, target=currentTarget)
print(*solution, "\n")
