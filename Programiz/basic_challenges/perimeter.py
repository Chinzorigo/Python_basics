'''
Compute Perimeter
Easy
Problem Description
Create a program to compute the perimeter of a triangle using OOP.

Create a Class

Create a class named Triangle that will have three attributes x, y, z.
Use the __init__() method to initialize attributes.
Create a method named get_perimeter() to compute the perimeter and return it.
Outside of the class

Take three integer inputs and assign them to a, b and c respectively. These are the sides of a triangle.
Create an object of the Triangle class with these values.
Call the get_perimeter() method using the object which returns the perimeter.
Print the perimeter.
Example
Test Input

1
2
3
Expected Output

6

'''


class Triangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_perimeter(self):
        return self.x + self.y + self.z


a = int(input())
b = int(input())
c = int(input())

t = Triangle(a, b, c)
print(t.get_perimeter())
