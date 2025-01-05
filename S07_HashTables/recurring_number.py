########################################################################################################################
### Data Structures and Algorithms :: Section 07
### Exercise: First Recurring Number
########################################################################################################################

### imports ############################################################################################################

from typing import List, Set

### solution using hash table ##########################################################################################
def first_recurring_number(aNums: List[int]=list()) -> int:
    """
    Interview Question: Given an array of integers, return the first recurring number.

    Args:
    - aNums : List[int], list of unsorted integers, defaults to empty list

    The solution uses a Python Set (hash table):
    - Time Complexity: O(n)
    - Space Complexity: O(n)

    Returns:
    - int, first recurring number in input array | None, if no recurring number is found
    """

    ### verifying inputs -----------------------------------------------------------------------------------------------

    if type(aNums) is not list or len(aNums) < 2: aNums = list()

    ### solution logic -------------------------------------------------------------------------------------------------

    nums_hash: Set[int] = set()
    for num in aNums:
        if type(num) is not int: continue
        if num in nums_hash: return num
        nums_hash.add(num)
        print(nums_hash)
    return

### testing code #######################################################################################################

print()
print("test ", first_recurring_number(aNums="test"), "\n")
print("[] ",first_recurring_number(aNums=[]), "\n")
print("[1] ", first_recurring_number(aNums=[1]), "\n")
print("[1,2] ", first_recurring_number(aNums=[1,2]), "\n")
print("[1,1] ", first_recurring_number(aNums=[1,1]), "\n")
print("[2,5,1,3,5,1,2,4] ", first_recurring_number(aNums=[2,5,1,3,5,1,2,4]), "\n")
