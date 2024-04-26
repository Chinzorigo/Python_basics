from collections import deque

queue = deque()  # Use deque for efficient queue operations

while True:
    command = input()
    if command == "End":
        break

    if command == "Paid":
        while queue:
            print(queue.popleft())  # Serve customers in order
    else:
        queue.append(command)  # Add new customer to the queue

print(f"{len(queue)} people remaining.")
