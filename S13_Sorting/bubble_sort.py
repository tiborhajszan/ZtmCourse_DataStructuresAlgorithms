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

    for counter in range(1, len(inputArray)):
        for index in range(0, len(inputArray)-counter):
            if inputArray[index] > inputArray[index+1]:
                inputArray[index], inputArray[index+1] = inputArray[index+1], inputArray[index]
    return

########################################################################################################################
### Testing Code
########################################################################################################################

print()
intArray: List[int] = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print("Unsorted:", intArray, "\n")
bubbleSort(inputArray=intArray)
print("Bubble Sort:", intArray, "\n")
