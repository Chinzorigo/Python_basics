# Define main and secondary colors
main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}
colors = []

# Take input from the user
input_string = input("Enter the string: ")

# Process input string
substrings = input_string.split()
while substrings:
    first = substrings[0]
    last = substrings[-1]

    # Check if either of the substrings is empty
    if not first or not last:
        break

    color = first[0] + last[-1]
    if color in main_colors:
        colors.append(color)
        substrings = substrings[1:-1]
    elif len(substrings) > 1:
        substrings[0] = first[:-1]
        substrings[-1] = last[:-1]
        substrings.insert(len(substrings) // 2, first[-1] + last[0])
    else:
        colors.append(color)
        break

# Collect colors
result = []
for color in colors:
    if color in secondary_colors:
        if color == "orange":
            if "red" in result and "yellow" in result:
                result.append(color)
        elif color == "purple":
            if "red" in result and "blue" in result:
                result.append(color)
        elif color == "green":
            if "yellow" in result and "blue" in result:
                result.append(color)
    else:
        result.append(color)

# Output the collected colors
print(result)
