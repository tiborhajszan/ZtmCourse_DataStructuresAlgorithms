########################################################################################################################
### Data Structures and Algorithms :: Section 04
### Exercise: Interview Question
########################################################################################################################

### brute force solution ###############################################################################################
def common_item_brute(array1=[], array2=[]):
    """
    Interview Question:
    Find out whether two arrays of strings have a common item.
    Return True if common item exists, return False otherwise.
    
    This solution uses a cross-comparison approach with nested loops.
    Time Complexity: O(a*b)
    Space Complexity: O(1)

    Args:
    - array1: List[str], first array
    - array2: List[str], second array

    Returns:
    - int, 1 = common item exists | 0 = no common item | -1 = invalid input
    """

    ### function init --------------------------------------------------------------------------------------------------

    # input array not list > returning -1
    if type(array1) is not list or type(array2) is not list: return -1 # tO(1)
    # input array empty > returning 0
    if len(array1) == 0 or len(array2) == 0: return 0 # tO(1)
    # input array item not string > returning -1
    if any(type(item) is not str for item in array1): return -1 # tO(a)
    if any(type(item) is not str for item in array2): return -1 # tO(b)

    ### function logic -------------------------------------------------------------------------------------------------

    # common item exists > returning 1
    if any(item in array1 for item in array2): return 1 # tO(a*b)
    # no common item > returning 0
    else: return 0 # tO(1)

### solution using python sets #########################################################################################
def common_item_sets(array1=[], array2=[]):
    """
    Interview Question:
    Find out whether two arrays of strings have a common item.
    Return True if common item exists, return False otherwise.

    This solution uses Python sets for better performance.
    Time complexity: O(a+b)
    Space complexity: O(a)

    Args:
    - array1: List[str], first array
    - array2: List[str], second array

    Returns:
    - int, 1 = common item exists | 0 = no common item | -1 = invalid input
    """

    ### function init --------------------------------------------------------------------------------------------------

    # input array not list > returning -1
    if type(array1) is not list or type(array2) is not list: return -1 # tO(1)
    # input array empty > returning 0
    if len(array1) == 0 or len(array2) == 0: return 0 # tO(1)
    # input array item not string > returning -1
    if any(type(item) is not str for item in array1): return -1 # tO(a)
    if any(type(item) is not str for item in array2): return -1 # tO(b)

    ### function logic -------------------------------------------------------------------------------------------------

    # converting array1 to set
    set1 = set(array1) # tO(a) sO(a)
    # common item exists > returning 1
    if any(item in set1 for item in array2): return 1 # tO(b)
    # no common item > returning 0
    else: return 0 # tO(1)

### calling function ###################################################################################################

array1 = ["a", "b", "c", "x"]
array2 = ["z", "y", "w"]
print()
print(common_item_brute(array1=array1, array2=array2), "\n")
print(common_item_sets(array1=array1, array2=array2), "\n")
