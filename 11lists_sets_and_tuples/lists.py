

frutes = ["f1", "f2", "f3", "f4"]

for i in frutes:
    print(i)


print("appale" in frutes)
print("f1" in frutes)

frutes[0] = "3213142"
# frutes.remove("f1")
frutes.insert(2, "jj")

frutes.append("sjdlajs")

frutes.sort()
frutes.reverse()


print(frutes)
print(frutes.index("f2"))
print(frutes.count("f"))

frutes.clear()

print(frutes)
