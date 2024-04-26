numbers = input().split()
stack = []

for num in numbers:
    stack.append(num)

reversed_numbers = []
while stack:
    reversed_numbers.append(stack.pop())

print(" ".join(reversed_numbers))  # Print on one line with spaces
