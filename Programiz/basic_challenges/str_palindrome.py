"""
    Check if a string is a palindrome. do it with recursive function.

       """


def is_palindrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False


string = "radar"
print(is_palindrome(string))  # True
string = "level"
print(is_palindrome(string))  # True
string = "python"
print(is_palindrome(string))  # False
