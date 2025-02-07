########################################################################################################################
### Data Structures and Algorithms :: Section 13
### Merge Sort Implementation
########################################################################################################################

### imports ------------------------------------------------------------------------------------------------------------

from typing import List

########################################################################################################################
### Solution Functions
########################################################################################################################

### merge function #####################################################################################################
def merge(leftArray:List[int], rightArray:List[int]) -> List[int]:
    """
    Merges two sorted arrays of integers into a single sorted array.

    Args:
    - leftArray : List[int], left sorted array
    - rightArray : List[int], right sorted array

    Returns:
    - merged_array : List[int], merged sorted array
    """

    ### initializing merged array --------------------------------------------------------------------------------------

    merged_array: List[int] = list()

    ### merging arrays -------------------------------------------------------------------------------------------------

    while 0 < len(leftArray) + len(rightArray):
        if 0 < len(leftArray) and 0 < len(rightArray):
            if leftArray[0] < rightArray[0]: merged_array.append(leftArray.pop(0))
            else: merged_array.append(rightArray.pop(0))
        elif 0 < len(leftArray): merged_array.append(leftArray.pop(0))
        else: merged_array.append(rightArray.pop(0))
    
    ### returning merged array -----------------------------------------------------------------------------------------

    return merged_array

### merge sort function ################################################################################################
def merge_sort(sortArray:List[int]=list()) -> List[int]:
    """
    Sorts an array of integers using the Merge Sort algorithm.

    Args:
    - sortArray : List[int], array of integers to be sorted, defaults to empty list

    Returns:
    - sortArray : List[int], sorted array
    """

    ### invalid input > returning invalid input ------------------------------------------------------------------------

    if type(sortArray) is not list or len(sortArray) < 2: return sortArray
    if any(type(item) is not int for item in sortArray): return sortArray

    ### base case > returning sorted array -----------------------------------------------------------------------------

    if len(sortArray) == 1: return sortArray

    ### splitting array ------------------------------------------------------------------------------------------------

    middle_index: int = len(sortArray) // 2
    left_array: List[int] = sortArray[:middle_index]
    right_array: List[int] = sortArray[middle_index:]

    ### recursive case > returning sorted array ------------------------------------------------------------------------

    return merge(leftArray=merge_sort(sortArray=left_array), rightArray=merge_sort(sortArray=right_array))

########################################################################################################################
### Testing Code
########################################################################################################################

print()
print("Sort():", merge_sort())
print("Sort('test'):", repr(merge_sort(sortArray="test")))
print("Sort([42]):", merge_sort(sortArray=[42]))
print("Sort([99, 'test', 42]):", merge_sort(sortArray=[99, "test", 42]))
unsorted: List[int] = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print("Sort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]):", merge_sort(sortArray=unsorted), "\n")
