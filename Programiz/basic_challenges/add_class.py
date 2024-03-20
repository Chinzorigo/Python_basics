'''

Create a class

Create a class named Coordinate with attributes x and y.
Use the __init__() method with two arguments to initialize these attributes.
The class must also have a method named add_coordinates() that adds x and y attributes of two objects, then creates a new Coordinate object with these values, and returns the new Coordinate object.
Outside the class

Create two coordinates (objects of the Coordinate class) named c1 and c2.
The x and y attributes of c1 should be 5 and 6 respectively.
The x and y attributes of c2 should be 7 and 9 respectively.
Call add_coordinates() using the c1 object with c2 as an argument, and store the result to the c3 variable.
Print the x attribute of c3.
Print the y attribute of c3.
For hints, see the code outline.

'''

# create the Coordinate class


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add_coordinates(self, a, b):
        x = self.x + a.x + b.x
        y = self.y + a.y + b.y
        return Coordinate(x, y)


# create two Coordinate objects
c1 = Coordinate(5, 6)
c2 = Coordinate(7, 9)
c3 = Coordinate(1, 2)

# Call add_coordinates() using the c1 object with c2 as an argument, and store the result to the c3 variable.
c4 = Coordinate.add_coordinates(c1, c2, b)
c5 = c1.add_coordinates(c2, c3)

# print the x attribute of c3
print(c4.x)
print(c4.y)

print(c5.x)
print(c5.y)
