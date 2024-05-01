'''
Stacked Queries
You have an empty stack. You will receive an integer – N. On the next N lines, you will receive queries. Each query is one of these four types:
•	'1 {number}' – push the number (integer) into the stack
•	'2' – delete the number at the top of the stack
•	'3' – print the maximum number in the stack
•	'4' – print the minimum number in the stack
It is guaranteed that each query is valid.
After you go through all the queries, print the stack from top to bottom in the following format:
"{n}, {n1}, {n2}, ... {nn}"


'''

from collections import deque

stack = deque()

n = int(input())

for _ in range(n):

    query = input()

    if query.startswith("1"):
        number = int(query.split()[1])
        stack.append(number)
    elif query == "2":
        if stack:
            stack.pop()
    elif query == "3":
        if stack:
            print(max(stack))
    elif query == "4":
        if stack:
            print(min(stack))

stack = [str(x) for x in stack]

print(", ".join(stack[::-1]))
