# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
# print("You entered: ", x)


x = [1, 2, 1, 3, 4, 1, 2, 4, 1]

most_frequent = max(set(x), key=x.count)
print(most_frequent)

old = ['a', 'b', 'a', 'a', 'b', 'c']

new = list(dict.fromkeys(old))
print(new)

names = ['Peter', 'George', 'Amy', 'Alice']

# list comprehension for length of each name
lengths = [len(name) for name in names]
print(lengths)

# dictionary comprehension for name and length
name_length = {name: len(name) for name in names}
print(name_length)

x = range(1, 1000)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


primes = list(filter(is_prime, x))

print(primes)
