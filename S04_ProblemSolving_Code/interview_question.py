########################################################################################################################
### Data Structures and Algorithms :: Section 04
### Exercise: Interview Question
### --------------------------------------------------------------------------------------------------------------------
### Interview Question: Find out whether two arrays have a common item.
########################################################################################################################

### input arrays #######################################################################################################

array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'r']

### brute force solution ###############################################################################################
def common_item_1(array1=[], array2=[]):
    """
    Checks if two arrays have a common item.
    This solution is not ideal, because its time complexity: O(a*b) > O(n^2)

    Args:
    - array1: List[str], first array
    - array2: List[str], second array

    Returns:
    - bool, True = common item exists | False = no common item
    """

    # common item exists > returning true
    if any(item in array1 for item in array2): return True
    # no common item > returning false
    else: return False

### calling function ###################################################################################################

print("\n", common_item_1(array1=array1, array2=array2), "\n")
