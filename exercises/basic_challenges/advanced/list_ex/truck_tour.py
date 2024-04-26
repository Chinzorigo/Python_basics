from collections import deque


def can_complete_circle(petrol_pumps):
    petrol_tank = 0
    start_pump = 0

    for i in range(len(petrol_pumps)):
        petrol, distance = petrol_pumps[i]
        petrol_tank += petrol - distance

        if petrol_tank < 0:
            petrol_tank = 0
            start_pump = i + 1

    return start_pump if petrol_tank >= 0 else -1  # Return -1 if no solution


num_pumps = int(input())
pumps = deque()

for _ in range(num_pumps):
    petrol, distance = map(int, input().split())
    pumps.append((petrol, distance))

start_index = can_complete_circle(pumps)
print(start_index)
