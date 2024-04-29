# x = 10

# if x > 5:  # True
#     print("x > 5")


# if x > 10:  # False
#     print("x > 10")

# if x > 8:  # True
#     print("x > 8")


# else:
#     print("else will be executed")


x = 7

if x > 5:  # True
    if x == 6:  # False
        print("nested: x == 6")
    elif x == 10:  # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")
