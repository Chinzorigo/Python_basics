# a = set([1, 2, 3, 4,])
# b = set([3, 4, 5, 6, 7, 8, 9, 10])

# c = a > b
# print(c)


# set comprehension

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squared_nums = {num**2 for num in nums}
# print(squared_nums)

'''
The image provides instructions for a coding problem called "SoftUni Party." 
The task is to track guests who come to a party at SoftUni and identify those who did not attend based on their reservation codes. 
There are two types of guests: Regular and VIP. When a guest arrives, their reservation code is checked against two lists. 
The input consists of the number of guests N, followed by N reservation codes (8 characters long, VIP codes start with a digit). 
Then a list of guests who came to the party is provided until the "END" command. 
The output should print the number of guests who did not come and their reservation codes, with VIP codes listed first, and both VIP and Regular
 codes sorted in ascending order.
use regex.
'''

# Path: Programiz/basic_challenges/softuni_party.py

import re

n = int(input())
vip_guests = set()
regular_guests = set()

for _ in range(n):
    reservation_code = input()
    if re.match(r'\d', reservation_code[0]):
        vip_guests.add(reservation_code)
    else:
        regular_guests.add(reservation_code)

guests_arrived = set()

while True:
    guest = input()
    if guest == 'END':
        break
    guests_arrived.add(guest)

guests_not_arrived = (vip_guests | regular_guests) - guests_arrived
print(len(guests_not_arrived))
for guest in sorted(guests_not_arrived):
    print(guest)
