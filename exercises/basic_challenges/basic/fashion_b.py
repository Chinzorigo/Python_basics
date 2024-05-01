'''
Fashion Boutique
You own a fashion boutique and receive a delivery of a huge box of clothes, represented as a sequence of integers. On the following line, you will be given an integer representing the capacity for one rack in your store.  
You must arrange the clothes in the store and use the racks to hang up every piece of clothing. You start from the last piece of clothing on the top of the pile to the first one at the bottom. Use a stack for this purpose. Each piece of clothing has its value (an integer). You must sum their values while you take them out of the box:
•	If the sum becomes equal to the capacity of the current rack, you must take a new one for the next clothes (if there are any left in the box). 
•	If the sum becomes greater than the capacity, do not hang the piece of clothing on the current rack. Take a new rack and then hang it up.
In the end, print how many racks you have used to hang up the clothes.
Input
•	On the first line, you will be given a sequence of integers representing the clothes in the box, separated by a single space.
•	On the second line, you will be given an integer representing the capacity of a rack.
Output
•	Print the number of racks needed to hang up the clothes from the box.
Constraints
•	The values of the clothes will be integers in the range [0,20]
•	There will never be more than 50 clothes in a box
•	The capacity will be an integer in the range [0,20]
•	None of the integers from the box will be greater than the value of the capacity

Input
5 4 8 6 3 8 7 7 9
16
Output
5

Input
1 7 8 2 5 4 7 8 9 6 3 2 5 4 6
20
Output
5


'''

from collections import deque

clothes = deque(map(int, input().split()))
rack_capacity = int(input())

current_rack_capacity = rack_capacity
racks = 1

while clothes:
    current_clothes = clothes.pop()
    if current_clothes <= current_rack_capacity:
        current_rack_capacity -= current_clothes
    else:
        racks += 1
        current_rack_capacity = rack_capacity
        current_rack_capacity -= current_clothes

print(racks)
# Explanation:
# We start from the last piece of clothing and go to the first one. We take clothes from the box and hang them on the racks. If the sum of the clothes' values becomes equal to the capacity of the current rack, we take a new one. If the sum becomes greater than the capacity, we do not hang the current piece of clothing on the current rack. We take a new rack and hang it up. We continue this process until we have no clothes left in the box. In the end, we print the number of racks we have used to hang up all the clothes.
# In the first example, we need 5 racks to hang up all the clothes. The sum of the clothes' values on the first rack is 15, on the second rack is 14, on the third rack is 16, on the fourth rack is 15, and on the fifth rack is 9. The total number of racks is 5.
# In the second example, we need 5 racks to hang up all the clothes. The sum of the clothes' values on the first rack is 20, on the second rack is 20, on the third rack is 20, on the fourth rack is 20, and on the fifth rack is 20. The total number of racks is 5.
