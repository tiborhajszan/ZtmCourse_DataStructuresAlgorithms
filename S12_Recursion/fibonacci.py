########################################################################################################################
### Data Structures and Algorithms :: Section 12
### Fibonacci: Iterative and Recursive Implementations
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
def fibonacci_recursive(fibIndex:int=None) -> int:
    """
    Calculates a value, specified by the given index, in the Fibonacci sequence using recursion.

    Args:
    - fibIndex : int | None, index of Fibonacci sequence, defaults to None

    Returns:
    - int, specified Fibonacci value | None, if index is invalid
    """

    ### invalid arguments > returning none -----------------------------------------------------------------------------

    if type(fibIndex) is not int or fibIndex < 0: return None

    ### base case ------------------------------------------------------------------------------------------------------

    if fibIndex < 2: return fibIndex

    ### recursive case -------------------------------------------------------------------------------------------------

    return fibonacci_recursive(fibIndex-1) + fibonacci_recursive(fibIndex-2)


########################################################################################################################
### Code Tests
########################################################################################################################

print()
print([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144], "\n")

print("Iterative()", fibonacci_iterative())
print("Iterative('test')", fibonacci_iterative(fibIndex="test"))
print("Iterative(-1)", fibonacci_iterative(fibIndex=-1))
print("Iterative(0)", fibonacci_iterative(fibIndex=0))
print("Iterative(1)", fibonacci_iterative(fibIndex=1))
print("Iterative(2)", fibonacci_iterative(fibIndex=2))
print("Iterative(8)", fibonacci_iterative(fibIndex=8))
print(f"Iterative(35): {fibonacci_iterative(fibIndex=35):,}\n")

print("Recursive()", fibonacci_recursive())
print("Recursive('test')", fibonacci_recursive(fibIndex="test"))
print("Recursive(-1)", fibonacci_recursive(fibIndex=-1))
print("Recursive(0)", fibonacci_recursive(fibIndex=0))
print("Recursive(1)", fibonacci_recursive(fibIndex=1))
print("Recursive(2)", fibonacci_recursive(fibIndex=2))
print("Recursive(8)", fibonacci_recursive(fibIndex=8))
print(f"Recursive(35): {fibonacci_recursive(fibIndex=35):,}\n")
