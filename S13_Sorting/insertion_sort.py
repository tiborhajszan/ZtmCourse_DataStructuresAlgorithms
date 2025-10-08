########################################################################################################################
### Data Structures and Algorithms
### Section 13 | Insertion Sort Implementation
########################################################################################################################

from typing import List

### insertion sort function ############################################################################################

def insertionSort(inputArray:List[int]=list()) -> int:
    """
    Sorts an array of integers in ascending order using the Insertion Sort algorithm.

    Args:
    - inputArray : List[int], array of integers to be sorted, defaults to empty list

    Returns:
    - 0, sort success | -1, sort failure
    """

    ### invalid input > returning -1 -----------------------------------------------------------------------------------

    if type(inputArray) is not list or len(inputArray) < 2: return -1
    if any(type(item) is not int for item in inputArray): return -1

    ### sorting input array --------------------------------------------------------------------------------------------

    for current_index in range(1, len(inputArray)):
        for sort_index in range(current_index, 0, -1):
            if inputArray[sort_index-1] > inputArray[sort_index]:
                inputArray[sort_index-1], inputArray[sort_index] = inputArray[sort_index], inputArray[sort_index-1]
            else: break
    
    ### returning 0 ----------------------------------------------------------------------------------------------------

    return 0

########################################################################################################################
### Testing Code
########################################################################################################################

print()
intArray: List[int] = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print("Unsorted:", intArray)
print("Sorted:", insertionSort(inputArray=intArray), intArray)
print()
print("Sort():", insertionSort())
intArray = "test"
print("Sort('test'):", insertionSort(inputArray=intArray), repr(intArray))
intArray = [42]
print("Sort([42]):", insertionSort(inputArray=intArray), intArray)
intArray = [99, "test", 42]
print("Sort([99, 'test', 42]):", insertionSort(inputArray=intArray), intArray)
print()
