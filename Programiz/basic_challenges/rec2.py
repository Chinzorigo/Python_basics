# def display(n):

#     if n >= 4:
#         return 1

#     return display(n + 1) * 2


# print(display(1))


def display(n):

    if n == 4:
        return

    return display(n + 1) * 2


print(display(1))
