while True:
    try:
        text = input()
        times = int(input())
        print(text * times)
        break
    except ValueError:
        print("Invalid input. Please enter a string followed by an integer.")
