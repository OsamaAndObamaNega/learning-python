item = [["coconut", "pinapal", "appale"],
        ["2d sd2"]]

# print(item[1][0])
numpad = (("1","2","3"),("4","5","6"),("7","8","9"),(" ", "0"))

for i in item:
    for x in i:
        print(x)


for i in numpad:
    for j in i:
        print(j, end="  ")
    print()
