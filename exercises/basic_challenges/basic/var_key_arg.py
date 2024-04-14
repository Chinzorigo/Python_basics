'''

Problem Description
Write a program to create a function that can take a variable number of keyword arguments.

Create a function named full_name() that can take a variable number of keyword arguments.
Inside the function, print the arguments.
Outside the function

Take two string inputs and assign them to variables first and last respectively.
Call the full_name() function like this: full_name(first = first, last = last)
Example
Test Input

Joe
Biden
Expected Output

{'first':'joe', 'last': 'biden'}

'''


# create the function
def full_name(**kwargs):
    print(kwargs)


# take two string inputs
first = input().lower()
last = input().lower()

# call the function
full_name(first=first, last=last)
