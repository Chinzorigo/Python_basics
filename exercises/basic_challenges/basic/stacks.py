# reverse string using stack method which is append and pop

# def reverse_string(string):
#     string_list = list(string)
#     string_list.append(string_list.pop())
#     return ''.join(string_list)


# print(reverse_string("hello"))  # olleh


expression = '1 + (2-(2+3)*4/(3+1))*5'

parentheses = []

for i in range(len(expression)):
    if expression[i] == '(':
        parentheses.append(i)
    elif expression[i] == ')':
        loc = parentheses.pop()
        print(expression[loc:i+1])
