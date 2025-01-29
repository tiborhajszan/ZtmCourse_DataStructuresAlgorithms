########################################################################################################################
### Data Structures and Algorithms :: Section 06
### Exercise: Reverse A String
########################################################################################################################

### solution using array manipulation ##################################################################################
def reverse_string_array(forwardString=str()) -> str:
    """
    Reverses a string using array manipulation:
    - returns empty string if input type is not string;
    - returns forward string unchanged if forward string is less than 2 characters;
    - splits forward string into a forward array of characters;
    - loop: loads characters in reverse order into a reversed array;
    - joins the reversed array into a string and returns it.

    Args:
    - forwardString: str, string to reverse

    Returns:
    - str, reversed string
    """

    ### verifying input ------------------------------------------------------------------------------------------------

    if type(forwardString) is not str: return ""
    if len(forwardString) < 2: return forwardString

    ### main logic -----------------------------------------------------------------------------------------------------

    forward_array = list(forwardString)
    reversed_array = list()
    for index in range(len(forward_array) - 1, -1, -1): reversed_array.append(forward_array[index])
    return "".join(reversed_array)

### solution using slicing #############################################################################################
def reverse_string_slicing(forwardString=str()) -> str:
    """
    Reverses a string using string slicing:
    - returns empty string if input type is not string;
    - returns forward string unchanged if forward string is less than 2 characters;
    - reverses the forward string using string slicing and returns it.

    Args:
    - forwardString: str, string to reverse

    Returns:
    - str, reversed string
    """
    

    ### verifying input ------------------------------------------------------------------------------------------------

    if type(forwardString) is not str: return ""
    if len(forwardString) < 2: return forwardString

    ### main logic -----------------------------------------------------------------------------------------------------

    return forwardString[::-1]

### calling functions ##################################################################################################

reverse_string = reverse_string_array(forwardString="XO")
print("\n", [reverse_string], "\n")
reverse_string = reverse_string_slicing(forwardString="Hello world!")
print("\n", [reverse_string], "\n")
