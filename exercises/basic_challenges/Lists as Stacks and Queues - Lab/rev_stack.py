'''
    1. Reverse Strings
Write program that:
    • Reads an input string
    • Reverses it using a stack
    • Prints the result back on the console
Examples
Input
Output
I Love Python
nohtyP evoL I
Stacks and Queues
seueuQ dna skcatS


'''


text = list(input())
stack = []

for i in range(len(text)):
    stack.append(text.pop())

print(':'.join(stack))
print(stack)
