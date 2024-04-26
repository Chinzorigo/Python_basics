from collections import deque

kids = input().split()  # Get kids' names
nth_toss = int(input())  # Get the nth toss

circle = deque(kids)  # Create a queue (circle) of kids

while len(circle) > 1:
    circle.rotate(-(nth_toss - 1))  # Rotate the queue to skip kids
    removed_kid = circle.popleft()
    print(f"Removed {removed_kid}")

last_kid = circle.popleft()
print(f"Last is {last_kid}")
