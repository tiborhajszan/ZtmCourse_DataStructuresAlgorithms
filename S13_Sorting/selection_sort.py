########################################################################################################################
### Data Structures and Algorithms
### Section 13 | Selection Sort Implementation
########################################################################################################################

from typing import List

### selection sort function ############################################################################################

def selectionSort(inputArray:List[int]=list()) -> None:
    """
    Sorts an array of integers in ascending order using the Selection Sort algorithm.

    Args:
    - inputArray : List[int], array of integers to be sorted, defaults to empty list

    Returns:
    - 0, sort success | -1, sort failure
    """

    ### invalid input > returning -1 -----------------------------------------------------------------------------------

    if type(inputArray) is not list or len(inputArray) < 2: return -1
    if any(type(item) is not int for item in inputArray): return -1

    ### sorting input array --------------------------------------------------------------------------------------------

    for sorted_index in range(0, len(inputArray)-1):
        min_index = sorted_index
        for index in range(sorted_index+1, len(inputArray)):
            if inputArray[index] < inputArray[min_index]: min_index = index
        inputArray[sorted_index], inputArray[min_index] = inputArray[min_index], inputArray[sorted_index]
    
    ### returning 0 ----------------------------------------------------------------------------------------------------

    return 0

########################################################################################################################
### Testing Code
########################################################################################################################

print()
intArray: List[int] = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print("Unsorted:", intArray)
selectionSort(inputArray=intArray)
print("Sorted:", selectionSort(inputArray=intArray), intArray)
print()
print("Sort():", selectionSort())
intArray = "test"
print("Sort('test'):", selectionSort(inputArray=intArray), repr(intArray))
intArray = [42]
print("Sort([42]):", selectionSort(inputArray=intArray), intArray)
intArray = [99, "test", 42]
print("Sort([99, 'test', 42]):", selectionSort(inputArray=intArray), intArray)
print()
