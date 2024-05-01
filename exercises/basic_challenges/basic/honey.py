from collections import deque

bees = deque(map(int, input().split(" ")))
nectars = list(map(int, input().split(" ")))
symbols = deque(input().split(" "))
total_honey = 0

while bees and nectars:
    if bees[0] <= nectars[-1]:
        if symbols[0] == "+":
            total_honey += abs(bees[0] + nectars[-1])
        elif symbols[0] == "-":
            total_honey += abs(bees[0] - nectars[-1])
        elif symbols[0] == "*":
            total_honey += abs(bees[0] * nectars[-1])
        elif symbols[0] == "/":
            total_honey += abs(bees[0] / nectars[-1])
        bees.popleft()
        nectars.pop()
        symbols.popleft()
    else:
        nectars.pop()

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left:", end=" ")
    print(*bees, sep=", ")
if nectars:
    print(f"Nectar left:", end=" ")
    print(*nectars, sep=", ")
