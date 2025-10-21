########################################################################################################################
### Data Structures and Algorithms
### Section 13 | Bubble Sort Implementation
########################################################################################################################

from typing import List

### bubble sort function ###############################################################################################

def bubbleSort(inputArray:List[int]=list()) -> None:
    """
    Sorts an array of integers in ascending order using the Bubble Sort algorithm.

    Args:
    - inputArray : List[int], array of integers to be sorted, defaults to empty list

    Returns:
    - None
    """

    ### function init --------------------------------------------------------------------------------------------------

    if type(inputArray) is not list or len(inputArray) < 2: return
    if any(type(item) is not int for item in inputArray): return

    ### sorting array --------------------------------------------------------------------------------------------------

    for size in range(len(inputArray)-1, 1, -1):
        for index in range(0, size):
            if inputArray[index] > inputArray[index+1]:
                inputArray[index], inputArray[index+1] = inputArray[index+1], inputArray[index]
    
    ### function ends --------------------------------------------------------------------------------------------------

    return

########################################################################################################################
### Testing Code
########################################################################################################################

print()

int_array: List[int] = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 77, 66, 44]
print("Unsorted:", int_array)
bubbleSort(inputArray=int_array)
print("Sorted:", int_array)

print()

int_array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 77, 66, 44]
bubbleSort()
print("Sort():", int_array)

int_array = "test"
bubbleSort(inputArray=int_array)
print("Sort('test'):", repr(int_array))

int_array = [42]
bubbleSort(inputArray=int_array)
print("Sort([42]):", int_array)

int_array = [99, "test", 42]
bubbleSort(inputArray=int_array)
print("Sort([99, 'test', 42]):", int_array)

print()
