########################################################################################################################
### Data Structures and Algorithms :: Section 12
### Factorial: Iterative and Recursive Implementations
########################################################################################################################

########################################################################################################################
### Solution Functions
########################################################################################################################

### iterative solution #################################################################################################
def factorial_iterative(number:int=None) -> int:
    """
    Calculates the factorial of the given integer using iteration.

    Args:
    - number : int | None, base of factorial, defaults to None

    Returns:
    - factorial : int, factorial of given number | None, if number is invalid
    """

    ### invalid arguments > returning none -----------------------------------------------------------------------------

    if type(number) is not int or number < 0: return None

    ### number = 0,1,2 > returning number ------------------------------------------------------------------------------

    if number < 3: return number

    ### number = 2+ > calculating and returning factorial --------------------------------------------------------------

    factorial: int = number
    for integer in range(number-1, 1, -1): factorial *= integer
    return factorial

### recursive solution #################################################################################################
def factorial_recursive(number:int=None) -> int:
    """
    Calculates the factorial of the given integer using recursion.

    Args:
    - number : int | None, base of factorial, defaults to None

    Returns:
    - int, factorial of given number | None, if number is invalid
    """

    ### invalid arguments > returning none -----------------------------------------------------------------------------

    if type(number) is not int or number < 0: return None

    ### base case > returning number -----------------------------------------------------------------------------------

    if number < 3: return number

    ### recursive case > returning factorial ---------------------------------------------------------------------------

    return number * factorial_recursive(number-1)

########################################################################################################################
### Code Tests
########################################################################################################################

print()
print("Iterative()", factorial_iterative())
print("Iterative('test')", factorial_iterative(number="test"))
print("Iterative(-1)", factorial_iterative(number=-1))
print("Iterative(0)", factorial_iterative(number=0))
print("Iterative(1)", factorial_iterative(number=1))
print("Iterative(2)", factorial_iterative(number=2))
print("Iterative(5)", factorial_iterative(number=5))
print(f"Iterative(15): {factorial_iterative(number=15):,}\n")

print("Recursive()", factorial_recursive())
print("Recursive('test')", factorial_recursive(number="test"))
print("Recursive(-1)", factorial_recursive(number=-1))
print("Recursive(0)", factorial_recursive(number=0))
print("Recursive(1)", factorial_recursive(number=1))
print("Recursive(2)", factorial_recursive(number=2))
print("Recursive(5)", factorial_recursive(number=5))
print(f"Recursive(15): {factorial_recursive(number=15):,}\n")
