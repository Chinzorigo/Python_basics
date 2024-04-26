'''
Lab: Lists as Stacks and Queues 
Problems for in-class lab for the Python Advanced Course @SoftUni Global 
Submit your solutions in the SoftUni Judge System 
Reverse Strings 
Write program that: 
Reads an input string 
Reverses it using a stack 
Prints the result back on the console 

Examples 
Input 
I Love Python 
Stacks and Queues 
Output 
nohtyP evoL I 
seueuQ dna skcatS 

'''


string = input()
stack = []

for ch in string:
    stack.append(ch)

reversed_string = ''
while stack:
    reversed_string += stack.pop()

print(reversed_string)
