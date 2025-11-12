########################################################################################################################
### Data Structures And Algorithms
### Section 13 | Merge Sort Implementation
########################################################################################################################

from typing import List

### merge arrays function ##############################################################################################

def mergeArrays(leftArray:List[int], rightArray:List[int]) -> List[int]:
    """
    Merges two sorted arrays of integers into a single sorted array.

    Args:
    - leftArray : List[int], left sorted array to merge
    - rightArray : List[int], right sorted array to merge

    Returns:
    - List[int], merged sorted array
    """

    ### function init --------------------------------------------------------------------------------------------------

    merged_array: List[int] = list()

    ### merging arrays -------------------------------------------------------------------------------------------------

    while 0 < len(leftArray) + len(rightArray):
        if 0 < len(leftArray) and 0 < len(rightArray):
            if leftArray[0] < rightArray[0]: merged_array.append(leftArray.pop(0))
            else: merged_array.append(rightArray.pop(0))
        elif 0 < len(leftArray): merged_array.append(leftArray.pop(0))
        else: merged_array.append(rightArray.pop(0))
    
    ### returning merged sorted array ----------------------------------------------------------------------------------

    return merged_array

### merge sort function ################################################################################################

def mergeSort(inputArray:List[int]=list()) -> List[int]:
    """
    Sorts an array of integers in ascending order using the Merge Sort algorithm.

    Args:
    - inputArray : List[int], array of integers to be sorted, defaults to empty list

    Returns:
    - List[int], sorted array
    """

    ### invalid input | base case > returning input array --------------------------------------------------------------

    if type(inputArray) is not list or len(inputArray) < 2: return inputArray
    if any(type(item) is not int for item in inputArray): return inputArray

    ### recursive case > splitting input array -------------------------------------------------------------------------

    middle_index: int = len(inputArray) // 2
    left_array: List[int] = mergeSort(inputArray[:middle_index])
    right_array: List[int] = mergeSort(inputArray[middle_index:])

    ### returning merged sorted array ----------------------------------------------------------------------------------

    return mergeArrays(leftArray=left_array, rightArray=right_array)

########################################################################################################################
### Testing Code
########################################################################################################################

print()

int_array: List[int] = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 77, 66, 44, 44]
print("Unsorted:", int_array)
print("Sorted:", mergeSort(inputArray=int_array))

print()

int_array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 77, 66, 44, 44]
print("Sort():", mergeSort())

int_array = "test"
print("Sort('test'):", repr(mergeSort(inputArray=int_array)))

int_array = [42]
print("Sort([42]):", mergeSort(inputArray=int_array))

int_array = [99, "test", 42]
print("Sort([99, 'test', 42]):", mergeSort(inputArray=int_array))

print()
