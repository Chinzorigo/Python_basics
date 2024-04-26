from collections import deque

food_quantity = int(input())  # Get initial food quantity
# Get orders as a queue of ints
orders = deque([int(x) for x in input().split()])

biggest_order = max(orders)
print(biggest_order)

while orders:
    current_order = orders[0]
    if current_order <= food_quantity:
        food_quantity -= current_order
        orders.popleft()
    else:
        break  # Not enough food, stop serving

if not orders:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(str(x) for x in orders)}")
