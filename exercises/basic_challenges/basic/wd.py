'''
4.	Water Dispenser
Write a program that keeps track of people getting water from a dispenser and the amount of water left at the end. 
On the first line, you will receive the starting quantity of water (integer) in a dispenser. Then, on the following lines, you will be given the names of some people who want to get water (each on a separate line) until you receive the command "Start". Add those people in a queue. Finally, you will receive some commands until the command "End":
-	"{liters}" - litters (integer) that the current person in the queue wants to get. Check if there is enough water in the dispenser for that person.
o	If there is enough water, print "{person_name} got water" and remove him/her from the queue.
o	Otherwise, print "{person_name} must wait" and remove the person from the queue without reducing the water in the dispenser.
-	"refill {liters}" - add the given litters in the dispenser.
In the end, print how many liters of water have left in the format: "{left_liters} liters left".
Examples
Input
2
Peter
Amy
Start
2
refill 1
1
End	Peter got water
Amy got water
comment
0 liters left	We create a queue with Peter and Amy. After the start command, we see that Peter wants 2 liters of water (and he gets them). The water dispenser is left with 0 liters. After refilling, there is 1 liter in the dispenser. So when Amy wants 1 liter, she gets it, and there are 0 liters left in the dispenser.
input
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
output
Peter got water
George got water
Amy got water
Alice must wait
2 liters left	


'''

from collections import deque

water = int(input())
people = deque()

while True:
    command = input()
    if command == "Start":
        break
    people.append(command)

while True:
    command = input()
    if command == "End":
        break
    if command.startswith("refill"):
        water += int(command.split()[1])
    else:
        person = people.popleft()
        if water >= int(command):
            print(f"{person} got water")
            water -= int(command)
        else:
            print(f"{person} must wait")


print(f"{water} liters left")
