########################################################################################################################
### Data Structures And Algorithms
### Section 15 | Fibonacci Function | Recursive Coding Pattern
########################################################################################################################

import random
calculations: int = 0

### recursive fibonacci function #######################################################################################
def fibonacci_recursive(fibIndex:int=0) -> int:
    """
    Calculates a value in the Fibonacci Sequence using recursion.

    ### Params:
    - fibIndex : int, index of fibonacci sequence  
        0 <= fibIndex <= 30  
        defaults to 0
    ### Returns:
    - int, fibonacci value
    - -1, invalid argument
    """

    ### invalid argument > returning -1 > incrementing & printing counter ----------------------------------------------

    if type(fibIndex) is not int or fibIndex < 0 or 30 < fibIndex: return -1
    global calculations; calculations += 1
    print(f"Calculations = {calculations:,}", end="\r")

    ### base case > fibonacci index 0,1 > returning fibonacci index ----------------------------------------------------

    if fibIndex < 2: return fibIndex

    ### recursive case -------------------------------------------------------------------------------------------------

    return fibonacci_recursive(fibIndex=fibIndex-1) + fibonacci_recursive(fibIndex=fibIndex-2)

########################################################################################################################
### testing code
########################################################################################################################

print()

print(f"Recursive Fibonacci() = {fibonacci_recursive()}")
print(f"Recursive Fibonacci('test') = {fibonacci_recursive(fibIndex='test')}")
print(f"Recursive Fibonacci(-1) = {fibonacci_recursive(fibIndex=-1)}")
print(f"Recursive Fibonacci(300) = {fibonacci_recursive(fibIndex=300)}")
print()

print(f"Recursive Fibonacci(0) = {fibonacci_recursive(fibIndex=0)}")
print(f"Recursive Fibonacci(1) = {fibonacci_recursive(fibIndex=1)}")
print()

calculations = 0
fib_index: int = random.randint(0, 30)
print(f"Fibonacci Index = {fib_index}")
print(f"\nRecursive Fibonacci({fib_index}) = {fibonacci_recursive(fibIndex=fib_index):,}")
print()
