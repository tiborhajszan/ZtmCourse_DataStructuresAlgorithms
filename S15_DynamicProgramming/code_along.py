########################################################################################################################
### Data Structures And Algorithms
### Section 15 | Dynamic Programming | Code Along
########################################################################################################################

from typing import Dict
global_cache: Dict[int, int] = dict()

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

    if inputInt in global_cache.keys(): return global_cache[inputInt]

    ### new input integer > calculating and caching new square ---------------------------------------------------------

    global_cache[inputInt] = inputInt ** 2
    
    ### returning cached new square------------------------------------------------------------------------------------

    return global_cache[inputInt]

### closure square function ############################################################################################
    
def square_closure():
    """
    Calculates the square of the input integer.  
    Demonstrates the closure coding pattern.

    ### Parameters
    - inputInt : int, input integer  
        -1000 <= inputInt <= 1000  
        defaults to 0
    ### Returns
    - int, square of input integer
    - -1, invalid argument
    """

    ### memoization init -----------------------------------------------------------------------------------------------

    private_cache: Dict[int, int] = dict()

    ### defining closure -----------------------------------------------------------------------------------------------

    def closure(inputInt:int=0) -> int:

        ### invalid argument > returning -1
        if type(inputInt) is not int or inputInt < -1000 or 1000 < inputInt: return -1

        ### known input integer > returning cached square
        if inputInt in private_cache.keys(): return private_cache[inputInt]

        ### new input integer > calculating and caching new square
        private_cache[inputInt] = inputInt ** 2
        
        ### returning cached new square
        return private_cache[inputInt]

    ### returning closure ----------------------------------------------------------------------------------------------

    return closure

########################################################################################################################
### testing code
########################################################################################################################

print()

print(f"Memoized Square() = {square_memoized()}")
print(f"Memoized Square('test') = {square_memoized(inputInt='test')}")
print(f"Memoized Square(-1001) = {square_memoized(inputInt=-1001)}")
print(f"Memoized Square(1001) = {square_memoized(inputInt=1001)}")
print()

print(f"Memoized Square(-1000) = {square_memoized(inputInt=-1000):,}")
print(f"Memoized Square(0) = {square_memoized(inputInt=0)}")
print(f"Memoized Square(1000) = {square_memoized(inputInt=1000):,}")
print()

print("-" * 20)
print()

print(f"Closure Square() = {square_closure()()}")
print(f"Closure Square('test') = {square_closure()(inputInt='test')}")
print(f"Closure Square(-1001) = {square_closure()(inputInt=-1001)}")
print(f"Closure Square(1001) = {square_closure()(inputInt=1001)}")
print()

print(f"Closure Square(-1000) = {square_closure()(inputInt=-1000):,}")
print(f"Closure Square(0) = {square_closure()(inputInt=0)}")
print(f"Closure Square(1000) = {square_closure()(inputInt=1000):,}")
print()
