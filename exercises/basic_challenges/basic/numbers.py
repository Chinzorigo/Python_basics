seq1 = set(map(int, input().split(" ")))
seq2 = set(map(int, input().split(" ")))

n = int(input())

for i in range(n):
    command = input().split(" ")
    if command[0] == "Add":
        if command[1] == "First":
            for num in range(2, len(command)):
                seq1.add(int(command[num]))
        elif command[1] == "Second":
            for num in range(2, len(command)):
                seq2.add(int(command[num]))
    elif command[0] == "Remove":
        if command[1] == "First":
            for num in range(2, len(command)):
                if int(command[num]) in seq1:
                    seq1.remove(int(command[num]))
        elif command[1] == "Second":
            for num in range(2, len(command)):
                if int(command[num]) in seq2:
                    seq2.remove(int(command[num]))
    elif command[0] == "Check" and command[1] == "Subset":
        if seq1 < seq2 or seq1 > seq2:
            print(True)
        else:
            print(False)

print(*sorted(seq1), sep=", ")
print(*sorted(seq2), sep=", ")
