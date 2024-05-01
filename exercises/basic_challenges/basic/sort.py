'''
Let's Sort This List!
Create a function that takes a list of numbers lst, a string s and return a list of numbers as per the following rules:

"Asc" returns a sorted list in ascending order.
"Des" returns a sorted list in descending order.
"None" returns a list without any modification.
Examples
asc_des_none([4, 3, 2, 1], "Asc" ) ➞ [1, 2, 3, 4]

asc_des_none([7, 8, 11, 66], "Des") ➞ [66, 11, 8, 7]

asc_des_none([1, 2, 3, 4], "None") ➞ [1, 2, 3, 4]
Notes
N/A

Test:

Test.assert_equals(asc_des_none([4, 3, 2, 1], "Asc"), [1, 2, 3, 4])
Test.assert_equals(asc_des_none([7, 8, 11, 66], "Des"), [66, 11, 8, 7])
Test.assert_equals(asc_des_none([1, 2, 3, 4], "None"),[1, 2, 3, 4])
Test.assert_equals(asc_des_none([1, 0, 1, 0], "Asc"), [0, 0, 1, 1])
Test.assert_equals(asc_des_none([1, 2, 2, 2, 2, 2, 2], "Des"), [2, 2, 2, 2, 2, 2, 1])
Test.assert_equals(asc_des_none([9, 7, 43, 11, 16, 111, 19], "Asc"), [7, 9, 11, 16, 19, 43, 111])

'''


def asc_des_none(lst, s):
    if s == "Asc":
        return sorted(lst)
    elif s == "Des":
        return sorted(lst, reverse=True)
    else:
        return lst


print(asc_des_none([4, 3, 2, 1], "Asc"))
print(asc_des_none([7, 8, 11, 66], "Des"))
print(asc_des_none([1, 2, 3, 4], "None"))
print(asc_des_none([1, 0, 1, 0], "Asc"))
print(asc_des_none([1, 2, 2, 2, 2, 2, 2], "Des"))
print(asc_des_none([9, 7, 43, 11, 16, 111, 19], "Asc"))
