
item = {
    "smoll size popcorn" : 10,
    "midium size popcorn" : 18,
    "midium size popcorn" : 30,
    "choclet" : 10,
    "snack" : 5,
}

print("------------------manu------------------")
for key,valu in item.items():
    print(f"{key:20}", f": ${valu:.2f}")
print("----------------------------------------")


while True:
    food = input("Select an item(q to quit)").lower()
    if food == "q":
        break
