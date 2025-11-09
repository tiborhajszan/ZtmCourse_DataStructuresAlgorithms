########################################################################################################################
### Data Structures And Algorithms
### Section 13 | Insertion Sort Implementation
########################################################################################################################

from typing import List

### insertion sort function ############################################################################################

def insertionSort(inputArray:List[int]=list()) -> None:
    """
    Sorts an array of integers in ascending order using the Insertion Sort algorithm.

    Args:
    - inputArray : List[int], array of integers to be sorted, defaults to empty list

    Returns:
    - None
    """

    ### invalid input > function ends ----------------------------------------------------------------------------------

    if type(inputArray) is not list or len(inputArray) < 2: return
    if any(type(item) is not int for item in inputArray): return

    ### sorting input array --------------------------------------------------------------------------------------------

    for current in range(1, len(inputArray)):
        for bubble in range(current, 0, -1):
            if inputArray[bubble-1] > inputArray[bubble]:
                inputArray[bubble-1], inputArray[bubble] = inputArray[bubble], inputArray[bubble-1]
            else: break
    
    ### function ends --------------------------------------------------------------------------------------------------

    return

########################################################################################################################
### Testing Code
########################################################################################################################

print()

int_array: List[int] = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 77, 66, 44]
print("Unsorted:", int_array)
insertionSort(inputArray=int_array)
print("Sorted:", int_array)

print()

int_array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 77, 66, 44]
insertionSort()
print("Sort():", int_array)

int_array = "test"
insertionSort(inputArray=int_array)
print("Sort('test'):", repr(int_array))

int_array = [42]
insertionSort(inputArray=int_array)
print("Sort([42]):", int_array)

int_array = [99, "test", 42]
insertionSort(inputArray=int_array)
print("Sort([99, 'test', 42]):", int_array)

print()
