########################################################################################################################
### Data Structures and Algorithms :: Section 13
### Selection Sort Implementation
########################################################################################################################

### imports ------------------------------------------------------------------------------------------------------------

from typing import List

########################################################################################################################
### Solution Function
########################################################################################################################

def selection_sort(sortArray:List[int]=list()) -> List[int]:
    """
    Sorts an array of integers using the Selection Sort algorithm.

    Args:
    - sortArray : List[int], array of integers to be sorted, defaults to empty list

    Returns:
    - sortArray : List[int], sorted array
    """

    ### invalid input > returning invalid input ------------------------------------------------------------------------

    if type(sortArray) is not list or len(sortArray) < 2: return sortArray
    if any(type(item) is not int for item in sortArray): return sortArray

    ### sorting array > returning sorted array -------------------------------------------------------------------------

    for sorted_index in range(0, len(sortArray)-1):
        min_index = sorted_index
        for index in range(sorted_index+1, len(sortArray)):
            if sortArray[index] < sortArray[min_index]: min_index = index
        sortArray[sorted_index], sortArray[min_index] = sortArray[min_index], sortArray[sorted_index]
    return sortArray

########################################################################################################################
### Testing Code
########################################################################################################################

print()
print("Sort():", selection_sort())
print("Sort('test'):", repr(selection_sort(sortArray="test")))
print("Sort([42]):", selection_sort(sortArray=[42]))
print("Sort([99, 'test', 42]):", selection_sort(sortArray=[99, "test", 42]))
unsorted: List[int] = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print("Sort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]):", selection_sort(sortArray=unsorted), "\n")
