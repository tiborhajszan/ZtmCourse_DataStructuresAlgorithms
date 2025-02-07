########################################################################################################################
### Data Structures and Algorithms :: Section 13
### Insertion Sort Implementation
########################################################################################################################

### imports ------------------------------------------------------------------------------------------------------------

from typing import List

########################################################################################################################
### Solution Function
########################################################################################################################

def insertion_sort(sortArray:List[int]=list()) -> List[int]:
    """
    Sorts an array of integers using the Insertion Sort algorithm.

    Args:
    - sortArray : List[int], array of integers to be sorted, defaults to empty list

    Returns:
    - sortArray : List[int], sorted array
    """

    ### invalid input > returning invalid input ------------------------------------------------------------------------

    if type(sortArray) is not list or len(sortArray) < 2: return sortArray
    if any(type(item) is not int for item in sortArray): return sortArray

    ### sorting array > returning sorted array -------------------------------------------------------------------------

    for item_index in range(1, len(sortArray)):
        for index in range(item_index, 0, -1):
            if sortArray[index-1] > sortArray[index]:
                sortArray[index-1], sortArray[index] = sortArray[index], sortArray[index-1]
            else: break
    return sortArray

########################################################################################################################
### Testing Code
########################################################################################################################

print()
print("Sort():", insertion_sort())
print("Sort('test'):", repr(insertion_sort(sortArray="test")))
print("Sort([42]):", insertion_sort(sortArray=[42]))
print("Sort([99, 'test', 42]):", insertion_sort(sortArray=[99, "test", 42]))
unsorted: List[int] = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print("Sort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]):", insertion_sort(sortArray=unsorted), "\n")
