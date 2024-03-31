from collections import deque

import numpy as np
import pandas as pd
import torch


dispenser = int(input("Enter the number of water: "))

customers = deque([])

# a flag variable to know if it starts dispersing water

_start = False

while True:
    cmd = input("Enter command: ")
    if cmd == 'End':
        print(f'{len(customers)} people remaining in the queue')
        break
    elif cmd == 'Paid':
        for i in range(len(customers)):
            print(f'{customers.popleft()} paid')
    elif cmd == 'Start':
        _start = True
    else:
        if _start:
            if dispenser == 0:
                print('Dispenser is empty')
                break
            dispenser -= 1
            customers.append(cmd)
            print(f'{cmd} added to the queue')
            print(customers)
            print()
        else:
            print('Dispenser is not started yet')
            print('Enter Start to start the dispenser')
            print()
