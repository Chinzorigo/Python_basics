import random

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi', 'lemon',
          'mango', 'nectarine', 'orange', 'pear', 'quince', 'raspberry', 'strawberry', 'tangerine', 'ugli', 'watermelon']

x = random.choice(fruits)
y = random.shuffle(fruits)

print("x:", x)
print("y:", y)
print("fruits:", fruits)
