

def hello(name):
    print(f"hello, {name}")


def getName(firstOrSecond):
    return input(f"Enter ur {firstOrSecond}: ")

def crate_fullName(firstName, SecondName):
    return firstName.capitalize() + " " + SecondName.capitalize()


firstname = getName("firstName")
secondname = getName("SecondName")

fullname = crate_fullName(firstname, secondname)

print(fullname)