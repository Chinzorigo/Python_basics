def is_balanced(expression):
    stack = []
    matching_pairs = {")": "(", "}": "{", "]": "["}

    for char in expression:
        if char in matching_pairs.values():  # Opening parenthesis
            stack.append(char)
        elif char in matching_pairs:  # Closing parenthesis
            if not stack or stack.pop() != matching_pairs[char]:
                return False  # Mismatch
    return not stack  # True if stack is empty (all parentheses matched)


expression = input()
if is_balanced(expression):
    print("YES")
else:
    print("NO")
