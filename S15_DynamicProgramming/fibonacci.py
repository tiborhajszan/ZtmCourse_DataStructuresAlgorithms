########################################################################################################################
### Data Structures And Algorithms
### Section 15 | Fibonacci Function | Dynamic, BottomUp Implementations
########################################################################################################################

from typing import List, Dict
calculations: int = 0

### dynamic fibonacci function #########################################################################################

def fibonacci_dynamic():
    """
    Wrapper for a closure structure.
    """

    ### memoization init -----------------------------------------------------------------------------------------------

    global calculations; calculations = 0
    cache: Dict[int, int] = dict()

    ### closure definition ---------------------------------------------------------------------------------------------
    
    def closure(fibonacciIndex:int=0) -> int:
        """
        Calculates a value in the Fibonacci sequence using dynamic programming.

        Args:
        - fibonacciIndex : int, index of Fibonacci sequence, defaults to 0
        Returns:
        - int, specified Fibonacci value | -1, Fibonacci index is invalid
        """

        ### invalid argument > returning -1
        if type(fibonacciIndex) is not int or fibonacciIndex < 0: return -1

        ### fibonacci index 0,1 > returning index
        if fibonacciIndex < 2: return fibonacciIndex

        ### known fibonacci index > returning cached value
        if fibonacciIndex in cache.keys(): return cache[fibonacciIndex]

        ### new fibonacci index > incrementing counter > calculating value > returning value
        global calculations; calculations += 1
        cache[fibonacciIndex] = closure(fibonacciIndex-2) + closure(fibonacciIndex-1)
        return cache[fibonacciIndex]
    
    ### returning closure ----------------------------------------------------------------------------------------------

    return closure

### fibonacci bottom up dynamic function ###############################################################################
    
def fibonacci_bottomUp(fibonacciIndex:int=0) -> int:
    """
    Calculates a value in the Fibonacci sequence using bottom up dynamic programming.

    Args:
    - fibonacciIndex : int, index of Fibonacci sequence, defaults to 0
    Returns:
    - int, specified Fibonacci value | -1, Fibonacci index is invalid
    """

    ### invalid argument > returning -1 > counter init -----------------------------------------------------------------

    if type(fibonacciIndex) is not int or fibonacciIndex < 0: return -1
    global calculations; calculations = 0

    ### fibonacci index 0,1 > returning fibonacci index ----------------------------------------------------------------

    if fibonacciIndex < 2: return fibonacciIndex

    ### calculating fibonacci sequence ---------------------------------------------------------------------------------

    fibonacci_sequence: List[int] = [0, 1]
    current_index: int = 2
    while current_index <= fibonacciIndex:
        fibonacci_sequence.append(fibonacci_sequence[current_index-2] + fibonacci_sequence[current_index-1])
        calculations += 1; current_index += 1
    
    ### returning fibonacci value --------------------------------------------------------------------------------------

    return fibonacci_sequence.pop()

########################################################################################################################
### testing code
########################################################################################################################

print()
print("Fibonacci Dynamic Programming")
print()

print("Dynamic()", fibonacci_dynamic()())
print("Dynamic('test')", fibonacci_dynamic()(fibonacciIndex="test"))
print("Dynamic(-1)", fibonacci_dynamic()(fibonacciIndex=-1))
print("Dynamic(300)", fibonacci_dynamic()(fibonacciIndex=300))
print("Calculations: ", calculations)

print()

print("BottomUp()", fibonacci_bottomUp())
print("BottomUp('test')", fibonacci_bottomUp(fibonacciIndex="test"))
print("BottomUp(-1)", fibonacci_bottomUp(fibonacciIndex=-1))
print("BottomUp(300)", fibonacci_bottomUp(fibonacciIndex=300))
print("Calculations: ", calculations)

print()
