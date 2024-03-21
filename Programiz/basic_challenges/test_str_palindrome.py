def is_palindrome(s):
    return s == s[::-1]


# Test cases
print(is_palindrome("radar"))  # True
print(is_palindrome("level"))  # True
print(is_palindrome("python"))  # False
print(is_palindrome(""))  # True (empty string is considered a palindrome)
print(is_palindrome("a"))  # True (single character is considered a palindrome)

#   add more test cases


print(is_palindrome("madam"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("world"))  # False
print(is_palindrome("a"))  # True
print(is_palindrome(""))  # True
print(is_palindrome("ab"))  # False
print(is_palindrome("aa"))  # True
print(is_palindrome("aba"))  # True
print(is_palindrome("abba"))  # True
print(is_palindrome("abcba"))  # True
print(is_palindrome("abcde"))  # False
print(is_palindrome("abcdcba"))  # True
print(is_palindrome("abcdedcba"))  # True
print(is_palindrome("abcdeddcba"))  # False
