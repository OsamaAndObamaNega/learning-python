name = input("enter ur name: ")
phoneNumber = input("Enter ur mobile number: ")

string_to_find1 = ' '

# result = len(name)
# result = name.find(string_to_find1)
# result = name.rfind(string_to_find1)
# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phoneNumber.count("-")
phoneNumber = phoneNumber.replace(" ","-")

# print(f"there are no result for \"{string_to_find1}\"" if result == -1 else result)

print(f"the name is {name}")
print(phoneNumber)
