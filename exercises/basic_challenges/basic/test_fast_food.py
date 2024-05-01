from collections import deque
import pytest


def test_fast_food():
    # Test case 1: Enough food for all orders
    food = 348
    orders = deque([20, 54, 30, 16, 7, 9])
    assert fast_food(food, orders) == (54, "Orders complete")

    # Test case 2: Not enough food for all orders
    food = 499
    orders = deque([57, 45, 62, 70, 33, 90, 88, 76, 100, 50])
    assert fast_food(food, orders) == (100, "Orders left: 76 100 50")

    # Test case 3: No orders
    food = 1000
    orders = deque([])
    assert fast_food(food, orders) == (0, "Orders complete")

    # Test case 4: Single order
    food = 50
    orders = deque([50])
    assert fast_food(food, orders) == (50, "Orders complete")

    # Test case 5: Food quantity is 0
    food = 0
    orders = deque([10, 20, 30])
    assert fast_food(food, orders) == (10, "Orders left: 10 20 30")


def fast_food(food, orders):
    max_order = max(orders)
    while orders:
        order = orders[0]
        if food >= order:
            food -= order
            orders.popleft()
        else:
            break
    if not orders:
        return max_order, "Orders complete"
    else:
        return max_order, f"Orders left: {' '.join(map(str, orders))}"


test_fast_food()
