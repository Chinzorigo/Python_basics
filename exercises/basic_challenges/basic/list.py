# initialize   1d list "temperature" with 25 elements (random numbers between -20 and 100 inclusive) without import random module and loop

temperature = [18, 23, 34, 343, 45, 36, 67, 123, 344, 45, 56,
               67, 78, 89, 90, -12, 23, 34, 45, 56, 67, 78, 9, 90, 100]

# temperature = [18, 23, 34, 343, 45, 36, 67, 123, 344, 45, 56,
#                67, 78, 89, 90, 12, 23, 34, 45, 56, 67, 78, 89, 90, 100]

# write a function that takes a list of numbers and returns the lowest number in the list without using the min() function


def lowest_number(numbers):
    lowest = numbers[0]
    for number in numbers:
        if number < lowest:
            lowest = number
    return lowest


l_num = lowest_number(temperature)
print(l_num)
