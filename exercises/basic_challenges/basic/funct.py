def func() -> str:
    try:
        raise Exception('An error occurred')
    except:
        return 'A'
    finally:
        return 'B'


print(func())
# What will be the output of the above code snippet?
# A
# B
# None
