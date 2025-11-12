########################################################################################################################
### Data Structures And Algorithms
### Section 13 | Quick Sort Implementation
########################################################################################################################

from typing import List

### arrange array function #############################################################################################

def arrangeArray(inputArray:List[int]) -> int:
    """
    Arranges smaller elements to the left and larger elements to the right of the pivot.
    Determines the pivot index.

    Args:
    - inputArray : List[int], array of integers to be arranged

    Returns:
    - int, index of pivot element
    """

    ### function init --------------------------------------------------------------------------------------------------

    pivot_init: int = len(inputArray) - 1
    pivot_current: int = int(0)

    ### rearranging input array ----------------------------------------------------------------------------------------

    for current in range(0, pivot_init):
        if inputArray[current] < inputArray[pivot_init]:
            if pivot_current != current:
                inputArray[pivot_current], inputArray[current] = inputArray[current], inputArray[pivot_current]
            pivot_current += 1
    inputArray[pivot_current], inputArray[pivot_init] = inputArray[pivot_init], inputArray[pivot_current]
    
    ### returning pivot index ------------------------------------------------------------------------------------------

    return pivot_current

### quick sort function ################################################################################################

def quickSort(inputArray:List[int]=list()) -> List[int]:
    """
    Sorts an array of integers in ascending order using the Quick Sort algorithm.

    Args:
    - inputArray : List[int], array of integers to be sorted, defaults to empty list

    Returns:
    - List[int], sorted array
    """

    ### invalid input | base case > returning input array --------------------------------------------------------------

    if type(inputArray) is not list or len(inputArray) < 2: return inputArray
    if any(type(item) is not int for item in inputArray): return inputArray

    ### recursive case > finding pivot and splitting input array -------------------------------------------------------

    pivot_index: int = arrangeArray(inputArray=inputArray)
    left_array: List[int] = quickSort(inputArray=inputArray[:pivot_index])
    right_array: List[int] = quickSort(inputArray=inputArray[pivot_index+1:])
    
    ### returning sorted array -----------------------------------------------------------------------------------------

    return left_array + [inputArray[pivot_index]] + right_array

########################################################################################################################
### Testing Code
########################################################################################################################

print()

int_array: List[int] = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 77, 66, 44, 44]
print("Unsorted:", int_array)
print("Sorted:", quickSort(inputArray=int_array))

print()

int_array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 77, 66, 44, 44]
print("Sort():", quickSort())

int_array = "test"
print("Sort('test'):", repr(quickSort(inputArray=int_array)))

int_array = [42]
print("Sort([42]):", quickSort(inputArray=int_array))

int_array = [99, "test", 42]
print("Sort([99, 'test', 42]):", quickSort(inputArray=int_array))

print()
