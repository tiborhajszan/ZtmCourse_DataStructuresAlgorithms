########################################################################################################################
### Data Structures And Algorithms
### Section 13 | Quick Sort Implementation
########################################################################################################################

from typing import List

### quick arrange function #############################################################################################

def quickArrange(inputArray:List[int], pivotIndex:int, leftIndex:int, rightIndex:int) -> int:
    """
    Arranges smaller items to the left and larger items to the right of the pivot.
    Determines the split index.

    Args:
    - inputArray : List[int], array of integers to be sorted
    - pivotIndex : int, index of pivot item
    - leftIndex : int, index of first subarray item 
    - rightIndex : int, index of last subarray item

    Returns:
    - split_index : int, new index of pivot
    """

    ### function init --------------------------------------------------------------------------------------------------

    pivot_value: int = inputArray[pivotIndex]
    split_index: int = leftIndex

    ### rearranging array ----------------------------------------------------------------------------------------------

    for index in range(leftIndex, rightIndex):
        if inputArray[index] < pivot_value:
            inputArray[split_index], inputArray[index] = inputArray[index], inputArray[split_index]
            split_index += 1
    
    ### placing pivot > returning split index --------------------------------------------------------------------------

    inputArray[split_index], inputArray[pivotIndex] = inputArray[pivotIndex], inputArray[split_index]
    return split_index

### quick sort function ################################################################################################

def quickSort(inputArray:List[int]=list(), leftIndex:int=0, rightIndex:int=0) -> None:
    """
    Sorts an array of integers in ascending order using the Quick Sort algorithm.

    Args:
    - inputArray : List[int], array of integers to be sorted, defaults to empty list
    - leftIndex : int, index of first subarray item, defaults to 0
    - rightIndex : int, index of last subarray item, defaults to 0

    Returns:
    - None
    """

    ### function init --------------------------------------------------------------------------------------------------

    if type(inputArray) is not list or len(inputArray) < 2: return
    if any(type(item) is not int for item in inputArray): return
    split_index: int = 0

    ### sorting array --------------------------------------------------------------------------------------------------

    if leftIndex < rightIndex:
        split_index = quickArrange(
            inputArray=inputArray,
            pivotIndex=rightIndex,
            leftIndex=leftIndex,
            rightIndex=rightIndex)
        quickSort(inputArray=inputArray, leftIndex=leftIndex, rightIndex=split_index-1)
        quickSort(inputArray=inputArray, leftIndex=split_index+1, rightIndex=rightIndex)
    
    ### function ends --------------------------------------------------------------------------------------------------

    return

########################################################################################################################
### Testing Code
########################################################################################################################

print()

int_array: List[int] = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 77, 66, 44]
print("Unsorted:", int_array)
quickSort(inputArray=int_array, leftIndex=0, rightIndex=len(int_array)-1)
print("Sorted:", int_array)

print()

int_array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 77, 66, 44]
quickSort()
print("Sort():", int_array)

int_array = "test"
quickSort(inputArray=int_array, leftIndex=0, rightIndex=len(int_array)-1)
print("Sort('test'):", repr(int_array))

int_array = [42]
quickSort(inputArray=int_array, leftIndex=0, rightIndex=len(int_array)-1)
print("Sort([42]):", int_array)

int_array = [99, "test", 42]
quickSort(inputArray=int_array, leftIndex=0, rightIndex=len(int_array)-1)
print("Sort([99, 'test', 42]):", int_array)

print()
