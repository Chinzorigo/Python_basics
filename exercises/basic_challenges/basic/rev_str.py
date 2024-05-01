'''
Find the Length of a String
Medium
Problem Description
Write a program to find the length of a string using recursion.

Create a function named find_length() that accepts a string argument, text.
Find the length of text in a recursive manner and return it.
Print the output.
Note: Don't use string's len() method to find the length of the string.

Example
Test Input

Spiderman
Expected Output

9

'''


def find_length(text):
    """
    Calculates the length of a given string recursively.

    Args:
        text (str): The input string.

    Returns:
        int: The length of the string.

    """
    if text == '':
        return 0
    return 1 + find_length(text[1:])


text = 'Spiderman'
print(find_length(text))
