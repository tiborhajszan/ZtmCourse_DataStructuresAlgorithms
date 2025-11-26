########################################################################################################################
### Data Structures And Algorithms
### Section 15 | Dynamic Fibonacci Function
########################################################################################################################

from typing import Dict
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

########################################################################################################################
### testing code
########################################################################################################################

print()

print("Fibonacci()", fibonacci_dynamic()())
print("Fibonacci('test')", fibonacci_dynamic()(fibonacciIndex="test"))
print("Fibonacci(-1)", fibonacci_dynamic()(fibonacciIndex=-1))

print()

print("Fibonacci(300)", fibonacci_dynamic()(fibonacciIndex=300))
print("Calculations: ", calculations)

print()
