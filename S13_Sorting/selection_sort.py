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
    - None
    """

    ### function init --------------------------------------------------------------------------------------------------

    if type(inputArray) is not list or len(inputArray) < 2: return
    if any(type(item) is not int for item in inputArray): return

    ### sorting input array --------------------------------------------------------------------------------------------

    for sort_index in range(0, len(inputArray)-1):
        min_index = sort_index
        for current_index in range(sort_index+1, len(inputArray)):
            if inputArray[min_index] > inputArray[current_index]: min_index = current_index
        inputArray[sort_index], inputArray[min_index] = inputArray[min_index], inputArray[sort_index]
    
    ### function ends --------------------------------------------------------------------------------------------------

    return

########################################################################################################################
### Testing Code
########################################################################################################################

print()

int_array: List[int] = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 77, 66, 44]
print("Unsorted:", int_array)
selectionSort(inputArray=int_array)
print("Sorted:", int_array)

print()

int_array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 77, 66, 44]
selectionSort()
print("Sort():", int_array)

int_array = "test"
selectionSort(inputArray=int_array)
print("Sort('test'):", repr(int_array))

int_array = [42]
selectionSort(inputArray=int_array)
print("Sort([42]):", int_array)

int_array = [99, "test", 42]
selectionSort(inputArray=int_array)
print("Sort([99, 'test', 42]):", int_array)

print()
