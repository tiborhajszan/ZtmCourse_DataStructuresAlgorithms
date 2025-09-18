########################################################################################################################
### Data Structures And Algorithms
### Section 13 | Quick Sort Implementation
########################################################################################################################

from typing import List
number_array: List[int] = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0, 77, 66, 44]

### sort split function ################################################################################################

def sortSplit(input_array:List[int], pivot_index:int, left_index:int, right_index:int) -> int:
    """
    Arranges smaller items to the left and larger items to the right of the pivot.
    Determines the split index.

    Args:
    - input_array : List[int]
    - pivot_index : int, index of pivot item
    - left_index : int, index of first item to be compared with pivot
    - right_index : int, index of last item to be compared with pivot

    Returns:
    - split_index : int, new index of pivot
    """

    ### function init --------------------------------------------------------------------------------------------------

    pivot_value: int = input_array[pivot_index]
    split_index: int = left_index

    ### sorting array --------------------------------------------------------------------------------------------------

    for index in range(left_index, right_index):
        if input_array[index] < pivot_value:
            input_array[split_index], input_array[index] = input_array[index], input_array[split_index]
            split_index += 1
    
    ### placing pivot > returning split index --------------------------------------------------------------------------

    input_array[split_index], input_array[pivot_index] = input_array[pivot_index], input_array[split_index]
    return split_index

### quick sort function ################################################################################################

def quickSort(input_array:List[int], left_index:int, right_index:int) -> None:
    """
    Sorts an array of integers using the Quick Sort algorithm.

    Args:
    - input_array : List[int]
    - left_index : int, index of first item to be sorted
    - right_index : int, index of last item to be sorted

    Returns:
    - None
    """

    ### function init --------------------------------------------------------------------------------------------------

    pivot_index: int = 0
    split_index: int = 0

    ### sorting array --------------------------------------------------------------------------------------------------

    if left_index < right_index:
        pivot_index = right_index
        split_index = sortSplit(
            input_array=input_array,
            pivot_index=pivot_index,
            left_index=left_index,
            right_index=right_index)
        quickSort(input_array, left_index, split_index-1)
        quickSort(input_array, split_index+1, right_index)
    
    ### returning ------------------------------------------------------------------------------------------------------

    return

########################################################################################################################
### Testing Code
########################################################################################################################

print()
print(number_array)
quickSort(input_array=number_array, left_index=0, right_index=len(number_array)-1)
print(number_array)
print()
