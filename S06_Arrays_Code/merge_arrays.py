########################################################################################################################
### Data Structures and Algorithms :: Section 06
### Lesson: Merge Sorted Arrays
########################################################################################################################

### brute force solution using array manipulation ######################################################################
def merge_arrays_brute(array1=[], array2=[]):
    """
    Merges two sorted arrays of integers into a single sorted array:
    - converts input arrays to empty lists if they are not lists;
    - filters input arrays to include only integers;
    - creates an empty merged array;
    - loops through both input arrays parallelly:
        - takes first items from both arrays and substitutes a larger value if the array is empty;
        - appends the smaller item to the merged array;
    - returns the merged array.

    Args:
    - array1: List[int], first sorted array, defaults to empty list
    - array2: List[int], second sorted array, defaults to empty list

    Returns:
    - merged_array: List[int], sorted array from merging array1 and array2
    """

    ### verifying inputs -----------------------------------------------------------------------------------------------

    if type(array1) is not list: array1 = []
    if type(array2) is not list: array2 = []
    array1 = [item for item in array1 if type(item) is int]
    array2 = [item for item in array2 if type(item) is int]

    ### merging arrays -------------------------------------------------------------------------------------------------

    merged_array = list()
    while 0 < len(array1) + len(array2):
        item1 = array1[0] if 0 < len(array1) else array2[0] + 1
        item2 = array2[0] if 0 < len(array2) else array1[0] + 1
        if item1 <= item2: merged_array.append(array1.pop(0))
        else: merged_array.append(array2.pop(0))
    return merged_array

### pythonic solition using list concatenation and re-sorting ##########################################################
def merge_arrays_concat(array1=[], array2=[]):
    """
    Merges two sorted arrays of integers into a single sorted array:
    - converts input arrays to empty lists if they are not lists;
    - filters input arrays to include only integers;
    - merges input arrays using list concatenation and re-sorting and returns the result.

    Args:
    - array1: List[int], first sorted array, defaults to empty list
    - array2: List[int], second sorted array, defaults to empty list

    Returns:
    - List[int], sorted array from merging array1 and array2
    """

    ### verifying inputs -----------------------------------------------------------------------------------------------

    if type(array1) is not list: array1 = []
    if type(array2) is not list: array2 = []
    array1 = [item for item in array1 if type(item) is int]
    array2 = [item for item in array2 if type(item) is int]

    ### merging arrays -------------------------------------------------------------------------------------------------

    return sorted(array1 + array2)

### calling functions ##################################################################################################

array1 = [0, "3", 4, 31]
array2 = [4, "6", 30, 44]
print()
print(array1, array2, "\n")
print(merge_arrays_brute(array1=array1, array2=array2), "\n")
print(merge_arrays_concat(array1=array1, array2=array2), "\n")
