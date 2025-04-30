name = input("enter ur name: ")

if len(name) < 12 and name.find(" ") == -1 and name.isalpha():
    print("valid username")
else:
    print("invalid username \n enter 'c' to show all of the reqummant of the usernaem \n or press enter to pass")
    a = input("Enter: ")
    if a == "c":
        print("1. The username can not be more then 12 digit\n2. The username must not have any spases\n3.the username must only have alphabet") 
    
    
