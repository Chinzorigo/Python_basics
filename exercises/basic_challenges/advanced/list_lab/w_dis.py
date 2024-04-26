from collections import deque

water_quantity = int(input())  # Initial water quantity
queue = deque()

while True:
    command = input()
    if command == "Start":
        break
    queue.append(command)  # Add people to the queue

while True:
    command = input()
    if command == "End":
        break

    if command.startswith("refill"):
        liters_to_add = int(command.split()[1])
        water_quantity += liters_to_add
    else:
        liters_needed = int(command)
        person = queue.popleft()
        if liters_needed <= water_quantity:
            water_quantity -= liters_needed
            print(f"{person} got water")
        else:
            print(f"{person} must wait")

print(f"{water_quantity} liters left")
