########################################################################################################################
### Data Structures And Algorithms
### Section 15 | Dynamic Programming | Code Along
########################################################################################################################

from typing import List, Dict
cache: Dict[int, int] = dict()

### memoized square function ###########################################################################################

def square_memoized(inputInt:int=0) -> int:
    """
    Calculates the square of the input integer.  
    Demonstrates the memoization coding pattern.

    ### Parameters
    - inputInt : int, input integer  
        -1000 <= inputInt <= 1000  
        defaults to 0
    ### Returns
    - int, square of input integer
    - -1, invalid argument
    """

    ### invalid argument > returning -1 --------------------------------------------------------------------------------

    if type(inputInt) is not int or inputInt < -1000 or 1000 < inputInt: return -1

    ### known input integer > returning cached square ------------------------------------------------------------------

    if inputInt in cache.keys(): return cache[inputInt]

    ### new input integer > calculating and caching new square ---------------------------------------------------------

    cache[inputInt] = inputInt ** 2
    
    ### returning cached new square ------------------------------------------------------------------------------------

    return cache[inputInt]

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

print("Memoized Square")
print()

print("Memoized Square() =", square_memoized())
print()

print("Memoized Square('test') =", square_memoized(inputInt="test"))
print("Memoized Square(-1001) =", square_memoized(inputInt=-1001))
print("Memoized Square(1001) =", square_memoized(inputInt=1001))
print()

print("Memoized Square(-1000) =", square_memoized(inputInt=-1000))
print("Memoized Square(0) =", square_memoized(inputInt=0))
print("Memoized Square(1000) =", square_memoized(inputInt=1000))

print()
