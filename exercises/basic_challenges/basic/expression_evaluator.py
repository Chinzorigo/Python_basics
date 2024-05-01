chocos = list(map(int, input().split(", ")))
milks = list(map(int, input().split(", ")))

milkshake = 0

while milkshake < 5:
    if chocos[-1] == milks[0]:
        milkshake += 1
        chocos.pop()
        milks.pop(0)
    elif chocos[-1] <= 0:
        chocos.pop()
    elif milks[0] <= 0:
        milks.pop(0)
    else:
        chocos[-1] -= 5
        milks.append(milks.pop(0))
    if len(chocos) == 0 or len(milks) == 0:
        break

if milkshake == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocos:
    print(f"Chocolate:", end=" ")
    print(*chocos, sep=", ")
else:
    print("Chocolate: empty")
if milks:
    print(f"Milk:", end=" ")
    print(*milks, sep=", ")
else:
    print("Milk: empty")
