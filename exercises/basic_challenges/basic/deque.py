# from collections import deque

# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")           # Terry arrives
# queue.append("Graham")          # Graham arrives
# queue.popleft()                 # The first to arrive now leaves
# queue.popleft()                 # The second to arrive now leaves
# print(queue)                    # Remaining queue in order of arrival


from collections import deque

customers = deque([])

while True:
    cmd = input("Enter command: ")
    if cmd == 'End':
        print(f'{len(customers)} people remaining in the queue')
        break
    elif cmd == 'Paid':
        for i in range(len(customers)):
            print(f'{customers.popleft()} paid')
    else:
        customers.append(cmd)
        print(f'{cmd} added to the queue')
        print(customers)
        print()
