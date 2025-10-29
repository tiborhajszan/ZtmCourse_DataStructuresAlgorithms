########################################################################################################################
### Data Structures And Algorithms
### Section 13 | Quick Sort Implementation
########################################################################################################################

from typing import List

### arrange array function #############################################################################################

def arrangeArray(inputArray:List[int], leftIndex:int, rightIndex:int) -> int:
    """
    Arranges smaller items to the left and larger items to the right of the pivot.
    Determines the pivot index.

    Args:
    - inputArray : List[int], array of integers to be sorted
    - leftIndex : int, index of first subarray item 
    - rightIndex : int, index of last subarray item

    Returns:
    - pivot_index : int, index of pivot item
    """

    ### function init --------------------------------------------------------------------------------------------------

    pivot_index: int = leftIndex

    ### rearranging input array ----------------------------------------------------------------------------------------

    for index in range(leftIndex, rightIndex):
        if inputArray[index] < inputArray[rightIndex]:
            inputArray[pivot_index], inputArray[index] = inputArray[index], inputArray[pivot_index]
            pivot_index += 1
    inputArray[pivot_index], inputArray[rightIndex] = inputArray[rightIndex], inputArray[pivot_index]
    
    ### returning pivot index ------------------------------------------------------------------------------------------

    return pivot_index

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
    pivot_index: int = 0

    ### base case > returning  -----------------------------------------------------------------------------------------

    if -1 < leftIndex - rightIndex: return

    ### rearranging input array ----------------------------------------------------------------------------------------

    pivot_index = arrangeArray(inputArray=inputArray, leftIndex=leftIndex, rightIndex=rightIndex)

    ### recursive case > splitting input array -------------------------------------------------------------------------

    quickSort(inputArray=inputArray, leftIndex=leftIndex, rightIndex=pivot_index-1)
    quickSort(inputArray=inputArray, leftIndex=pivot_index+1, rightIndex=rightIndex)
    
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
