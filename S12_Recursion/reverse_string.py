########################################################################################################################
### Data Structures and Algorithms :: Section 12
### Reversing a String: Iterative and Recursive Implementations
########################################################################################################################

########################################################################################################################
### Solution Functions
########################################################################################################################

### iterative solution #################################################################################################
def reverse_iterative(forwardString:str=str()) -> str:
    """
    Reverses the given string using an iterative algorithm.

    Args:
    - forwardString : str, string to reverse, defaults to empty string

    Returns:
    - str, reversed string
    """

    ### invalid arguments > returning error message --------------------------------------------------------------------

    if type(forwardString) is not str: return f"Error: {forwardString} is not a string..."

    ### no need to reverse > returning forward string ------------------------------------------------------------------

    if len(forwardString) < 2: return forwardString

    ### reversing string > returning reversed string -------------------------------------------------------------------

    reverse_string: str = str()
    for char in forwardString[::-1]: reverse_string += char
    return reverse_string

### recursive solution #################################################################################################
def reverse_recursive(forwardString:str=str()) -> str:
    """
    Reverses the given string using a recursive algorithm.

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

### testing reverse_iterative() function -------------------------------------------------------------------------------

print("Iterative():", repr(reverse_iterative()))
print("Iterative(42):", reverse_iterative(forwardString=42))
print("Iterative('X'):", repr(reverse_iterative(forwardString="X")))
print("Iterative('yoyo master'):", repr(reverse_iterative(forwardString="yoyo master")), "\n")

### testing reverse_recursive() function -------------------------------------------------------------------------------

print("Recursive():", repr(reverse_recursive()))
print("Recursive(42):", reverse_recursive(forwardString=42))
print("Recursive('X'):", repr(reverse_recursive(forwardString="X")))
print("Recursive('yoyo master'):", repr(reverse_recursive(forwardString="yoyo master")), "\n")
