########################################################################################################################
### Data Structures and Algorithms
### Section 13 | Merge Sort Implementation
########################################################################################################################

from typing import List

### merge array function ###############################################################################################

def mergeArray(leftArray:List[int]=list(), rightArray:List[int]=list()) -> List[int]:
    """
    Merges two sorted arrays of integers into a single sorted array.

    Args:
    - leftArray : List[int], left sorted array, defaults to empty list
    - rightArray : List[int], right sorted array, defaults to empty list

    Returns:
    - merged_array : List[int], merged sorted array
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
    
    ### returning merged array -----------------------------------------------------------------------------------------

    return merged_array

### merge sort function ################################################################################################

def mergeSort(inputArray:List[int]=list()) -> List[int]:
    """
    Sorts an array of integers in ascending order using the Merge Sort algorithm.

    Args:
    - inputArray : List[int], array of integers to be sorted, defaults to empty list

    Returns:
    - sorted_array : List[int], sorted array
    """

    ### invalid input | base case > returning input array --------------------------------------------------------------

    if type(inputArray) is not list or len(inputArray) < 2: return inputArray
    if any(type(item) is not int for item in inputArray): return inputArray

    ### splitting input array ------------------------------------------------------------------------------------------

    middle_index: int = len(inputArray) // 2
    left_array: List[int] = inputArray[:middle_index]
    right_array: List[int] = inputArray[middle_index:]

    ### recursive case > returning sorted array ------------------------------------------------------------------------

    return mergeArray(leftArray=mergeSort(inputArray=left_array), rightArray=mergeSort(inputArray=right_array))

########################################################################################################################
### Testing Code
########################################################################################################################

print()
intArray: List[int] = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print("Unsorted:", intArray)
print("Sorted:", mergeSort(inputArray=intArray))
print()
print("Sort():", mergeSort())
intArray = "test"
print("Sort('test'):", repr(mergeSort(inputArray=intArray)))
intArray = [42]
print("Sort([42]):", mergeSort(inputArray=intArray))
intArray = [99, "test", 42]
print("Sort([99, 'test', 42]):", mergeSort(inputArray=intArray))
print()
