########################################################################################################################
### Data Structures and Algorithms :: Section 12
### Factorial: Recursive and Iterative Implementations
########################################################################################################################

########################################################################################################################
### Solution Functions
########################################################################################################################

### recursive solution #################################################################################################
def factorial_recursive(number:int=None) -> int:
    """
    Calculates the factorial of the given integer using recursion.

    Args:
    - number : int | None, base of factorial, defaults to None

    Returns:
    - int, factorial of given number | None, if number is invalid
    """


    ### validating arguments -------------------------------------------------------------------------------------------

    if type(number) is not int or number < 0: return None

    ### base case ------------------------------------------------------------------------------------------------------

    if number < 3: return number

    ### recursive case -------------------------------------------------------------------------------------------------

    return number * factorial_recursive(number-1)

### iterative solution #################################################################################################
def factorial_iterative(number:int=None) -> int:
    """
    Calculates the factorial of the given integer using iteration.

    Args:
    - number : int | None, base of factorial, defaults to None

    Returns:
    - factorial : int, factorial of given number | None, if number is invalid
    """

    ### validating arguments -------------------------------------------------------------------------------------------

    if type(number) is not int or number < 0: return None

    ### base case > returning number -----------------------------------------------------------------------------------

    if number < 3: return number

    ### iterative case > returning factorial ---------------------------------------------------------------------------

    factorial: int = number
    for integer in range(number-1, 1, -1): factorial *= integer
    return factorial

########################################################################################################################
### Code Tests
########################################################################################################################

print()
print("Recursive()", factorial_recursive())
print("Recursive('test')", factorial_recursive(number="test"))
print("Recursive(-1)", factorial_recursive(number=-1))
print("Recursive(0)", factorial_recursive(number=0))
print("Recursive(1)", factorial_recursive(number=1))
print("Recursive(2)", factorial_recursive(number=2))
print("Recursive(5)", factorial_recursive(number=5))
print(f"Recursive(15): {factorial_recursive(number=15):,}\n")

print("Iterative()", factorial_iterative())
print("Iterative('test')", factorial_iterative(number="test"))
print("Iterative(-1)", factorial_iterative(number=-1))
print("Iterative(0)", factorial_iterative(number=0))
print("Iterative(1)", factorial_iterative(number=1))
print("Iterative(2)", factorial_iterative(number=2))
print("Iterative(5)", factorial_iterative(number=5))
print(f"Iterative(15): {factorial_iterative(number=15):,}\n")
