########################################################################################################################
### Data Structures and Algorithms :: Section 04
### Exercise: Google Interview
########################################################################################################################

### solution for sorted array ##########################################################################################
def google_interview_sorted(array=[], target=0):
    """
    Interview Question:
    Within a collection of sorted (ascending) integers, find a pair that adds up to a target sum.
    Return true if pair is found, return false otherwise.

    This function uses a two-pointer approach.

    Args:
    - array: List[int], list of integers sorted in ascending order
    - target: int, target sum to find in array

    Returns:
    - bool, True = pair is found | False = pair is not found
    """

    ### pointer init ---------------------------------------------------------------------------------------------------

    left = 0
    right = len(array) - 1

    ### search loop ----------------------------------------------------------------------------------------------------

    # loop while pointers have not met
    while left < right:

        # summing items
        sum = array[left] + array[right]
        # sum is less than target > moving left pointer
        if sum < target: left += 1
        # sum equals target > returning true
        elif sum == target: return True
        # sum is greater than target > moving right pointer
        else: right -= 1
    
    ### no pair found > returning false --------------------------------------------------------------------------------

    return False

### solution for unsorted array ########################################################################################
def google_interview_unsorted(array=[], target=0):
    """
    Interview Question:
    Within a collection of unsorted integers, find a pair that adds up to a target sum.
    Return true if pair is found, return false otherwise.

    This function uses a linear complement search approach.

    Args:
    - array: List[int], list of unsorted integers
    - target: int, target sum to find in array

    Returns:
    - bool, True = pair is found | False = pair is not found
    """

    ### function init --------------------------------------------------------------------------------------------------

    complements = set()

    ### search loop ----------------------------------------------------------------------------------------------------

    # looping through array
    for item in array:

        # if item in complements > returning true
        if item in complements: return True
        # item not in complements > adding item complement to complements
        else: complements.add(target - item)

    ### no pair found > returning false --------------------------------------------------------------------------------

    return False

### calling functions ##################################################################################################

print()
print(google_interview_sorted(array=[1, 2, 4, 9], target=8), "\n")
print(google_interview_unsorted(array=[1, 2, 3, 4, 5, 6], target=8), "\n")
