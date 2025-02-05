########################################################################################################################
### Data Structures and Algorithms :: Section 12
### Reversing a String: Iterative and Recursive Implementations
########################################################################################################################

### imports ------------------------------------------------------------------------------------------------------------

from typing import List

########################################################################################################################
### Solution Functions
########################################################################################################################

### iterative solution #################################################################################################
def fibonacci_iterative(fibIndex:int=None) -> int:
    """
    Calculates a value, specified by the given index, in the Fibonacci sequence using iteration.

    Args:
    - fibIndex : int | None, index of Fibonacci sequence, defaults to None

    Returns:
    - int, specified Fibonacci value | None, if index is invalid
    """

    ### invalid arguments > returning none -----------------------------------------------------------------------------

    if type(fibIndex) is not int or fibIndex < 0: return None

    ### sequence init > extending sequence > returning value -----------------------------------------------------------

    fib_sequence: List[int] = [0, 1]
    for index in range(2, fibIndex+1): fib_sequence.append(fib_sequence[index-1] + fib_sequence[index-2])
    return fib_sequence[fibIndex]

### recursive solution #################################################################################################
def reverse_recursive(forwardString:str=str()) -> str:
    """
    Reverses the given string using recursion.

    Args:
    - forwardString : str, string to reverse, defaults to empty string

    Returns:
    - str, reversed string
    """

    ### invalid arguments > returning error message --------------------------------------------------------------------

    if type(forwardString) is not str: return f"Error: {forwardString} is not a string..."

    ### base case ------------------------------------------------------------------------------------------------------

    if len(forwardString) < 2: return forwardString

    ### recursive case -------------------------------------------------------------------------------------------------

    return reverse_recursive(forwardString=forwardString[1:]) + forwardString[0]

########################################################################################################################
### Code Tests
########################################################################################################################

print()

# print("Iterative()", fibonacci_iterative())
# print("Iterative('test')", fibonacci_iterative(fibIndex="test"))
# print("Iterative(-1)", fibonacci_iterative(fibIndex=-1))
# print("Iterative(0)", fibonacci_iterative(fibIndex=0))
# print("Iterative(1)", fibonacci_iterative(fibIndex=1))
# print("Iterative(2)", fibonacci_iterative(fibIndex=2))
# print("Iterative(8)", fibonacci_iterative(fibIndex=8))
# print(f"Iterative(35): {fibonacci_iterative(fibIndex=35):,}\n")

### testing reverse_recursive() ----------------------------------------------------------------------------------------

print("Recursive():", repr(reverse_recursive()))
print("Recursive(42):", reverse_recursive(forwardString=42))
print("Recursive('X'):", repr(reverse_recursive(forwardString="X")))
print("Recursive('yoyo master'):", repr(reverse_recursive(forwardString="yoyo master")), "\n")
