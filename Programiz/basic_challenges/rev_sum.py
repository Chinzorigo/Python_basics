def calculate_sum(n):

    # base case
    if n == 1:
        return 1

    # Before: return calculate_sum(n-1)
    # Now: add n to the return value of recursive call
    return n + calculate_sum(n - 1)


result = calculate_sum(4)
print(result)

# Output: 10
