# Replace ___ with your code

numbers = [1, 2, 3, 4]
values = [10, 20, 30, 40]

# create the dictionary using comprehension

new_dict = {k: v for (k, v) in zip(numbers, values)}

# print the dictionary
print(new_dict)

hello = 'Hello world'

new_dict2 = {k: v for (k, v) in enumerate(hello)}

print(new_dict2)

new_dict3 = {k: v for (k, v) in enumerate(hello, start=1)}

print(new_dict3)

