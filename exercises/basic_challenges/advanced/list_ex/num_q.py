num_queries = int(input())
stack = []

for _ in range(num_queries):
    query = input().split()
    command = query[0]

    if command == "1":  # Push
        number = int(query[1])
        stack.append(number)
    elif command == "2" and stack:  # Delete (only if stack is not empty)
        stack.pop()
    elif command == "3" and stack:  # Print max
        print(max(stack))
    elif command == "4" and stack:  # Print min
        print(min(stack))

print(", ".join(str(x) for x in reversed(stack)))  # Print stack bottom to top
