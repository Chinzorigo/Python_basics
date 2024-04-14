'''
Follow Google Python Style Guide
Allowed working time: 0.150 sec
Allowed memory: 16.00 MB
Size limit: 16.00 KB
Checker: Trim 

Supermarket:
Tom is working at the supermarket, and he needs your help to keep track of his clients. 
Write a program that reads lines of input consisting of a customer's name and adds it to 
the end of a queue until "End" is received. 
If, in the meantime, you receive the command "Paid", 
you should print each customer in the order they are served (from the first to the last one) 
and empty the queue. 
When you receive "End", you should print the count of the remaining people in the queue in the 
  format: "{count} people remaining.".


Examples:
1.Input

George
Peter
William
Paid
Michael
Oscar
Olivia
Linda
End
Output
George
Peter
William
4 people remaining.
2. Input:
Anna
Emma
Alexander
End

Output:
3 people remaining.
    


'''
from collections import deque
queue = deque()
while True:
    command = input()
    if command == "Paid":
        while len(queue):
            print(queue.popleft())

    elif command == "End":
        print(f"{len(queue)} people remaining.")
        break
    else:
        queue.append(command)


# customers = ['George', 'Peter', 'William', 'Michael', 'Oscar', 'Olivia', 'Linda']
