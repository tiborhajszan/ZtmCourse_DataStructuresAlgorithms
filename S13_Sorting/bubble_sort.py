########################################################################################################################
### Data Structures and Algorithms :: Section 13
### Bubble Sort Implementation
########################################################################################################################

### imports ------------------------------------------------------------------------------------------------------------

from typing import List

########################################################################################################################
### Solution
########################################################################################################################

def bubble_sort(sortArray:List[int]=list()) -> List[int]:
    """
    Sorts an array of integers using the Bubble Sort algorithm.

    Args:
    - sortArray : List[int], array of integers to be sorted, defaults to empty list

    Returns:
    - sortArray : List[int], sorted array
    """

    for counter in range(1, len(sortArray)):
        for index in range(0, len(sortArray)-counter):
            if sortArray[index] > sortArray[index+1]:
                sortArray[index], sortArray[index+1] = sortArray[index+1], sortArray[index]
    return sortArray

########################################################################################################################
### Testing Code
########################################################################################################################

print()
print("Unsorted:", [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0], "\n")
print("Bubble Sort:", bubble_sort(sortArray=[99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]), "\n")
