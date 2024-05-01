class Person:
    def __init__(self, name, age, hair_color, eye_color):
        print("Creating a new instance of Person class!")
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.eye_color = eye_color


person1 = Person(hair_color="Black", name="Badmaa", age=25, eye_color="Brown")

print(f'{person1.name} has {person1.hair_color} hair and {person1.eye_color} eyes. He is {person1.age} years old.')

person1.name = "Baatar"

print(f'{person1.name} has {person1.hair_color} hair and {person1.eye_color} eyes. He is {person1.age} years old.')
