clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

stack = []
racks_used = 1  # Start with one rack

while clothes:
    current_cloth = clothes.pop()
    if sum(stack) + current_cloth <= rack_capacity:
        stack.append(current_cloth)
    else:
        racks_used += 1
        stack.clear()  # New rack, empty the stack
        stack.append(current_cloth)

print(racks_used)
