from collections import deque

materials = list(map(int, input().split(" ")))
magics = deque(map(int, input().split(" ")))

toys = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

result = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0
}

while materials and magics:
    res = materials[-1] * magics[0]
    if res in toys:
        result[toys[res]] += 1
        materials.pop()
        magics.popleft()
    elif res < 0:
        m = materials.pop()
        p = magics.popleft()
        materials.append(m + p)
    elif materials[-1] == 0 or magics[0] == 0:
        if materials[-1] == 0:
            materials.pop()
        if magics[0] == 0:
            magics.popleft()
    elif res not in toys:
        magics.popleft()
        materials[-1] += 15

if (result["Doll"] > 0 and result["Wooden train"] > 0) or (result["Teddy bear"] > 0 and result["Bicycle"] > 0):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print("Materials left",  end=" ")
    print(*reversed(materials), sep=", ")
if magics:
    print("Magic left",  end=" ")
    print(*magics, sep=", ")

for p in sorted(result):
    if result[p] > 0:
        print(f"{p}: {result[p]}")
