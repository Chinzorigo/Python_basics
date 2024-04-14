'''
Follow Google Python Style Guide
Allowed working time: 0.150 sec
Allowed memory: 16.00 MB
Size limit: 16.00 KB
Checker: Trim 

Water Dispenser
Write a program that keeps track of people getting water from a dispenser and the amount of water left at the end. 
On the first line, you will receive the starting quantity of water (integer) in a dispenser. Then, on the following lines, you will be given the names of some people who want to get water (each on a separate line) until you receive the command "Start". Add those people in a queue. Finally, you will receive some commands until the command "End":
    • "{liters}" - litters (integer) that the current person in the queue wants to get. Check if there is enough water in the dispenser for that person.
        ◦ If there is enough water, print "{person_name} got water" and remove him/her from the queue.
        ◦ Otherwise, print "{person_name} must wait" and remove the person from the queue without reducing the water in the dispenser.
    • "refill {liters}" - add the given litters in the dispenser.
In the end, print how many liters of water have left in the format: "{left_liters} liters left".
Examples
Input:
2
Peter
Amy
Start
2
refill 1
1
End
Output
Peter got water
Amy got water
0 liters left
#We create a queue with Peter and Amy. After the start command, we see that Peter wants 2 liters of water (and he gets them). The water dispenser is left with 0 liters. After refilling, there is 1 liter in the dispenser. So when Amy wants 1 liter, she gets it, and there are 0 liters left in the dispenser.

Input:
10
Peter
George
Amy
Alice
Start
2
3
3
3
End
Output:
Peter got water
George got water
Amy got water
Alice must wait
2 liters left



'''


from collections import deque
water = int(input())
queue = deque()
while True:
    command = input()
    if command == "Start":
        break
    queue.append(command)
while True:
    command = input()
    if command == "End":
        break
    if command.startswith("refill"):
        refill = int(command.split()[1])
        water += refill
    else:
        liters = int(command)
        person = queue.popleft()
        if liters <= water:
            print(f"{person} got water")
            water -= liters
        else:
            print(f"{person} must wait")

print(f"{water} liters left")
