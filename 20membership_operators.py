word = "102"


letter = input("Enter to chack dsoe the letter is in the word: ")

if letter not in word:
    print("yes", word.find(letter))
else:
    print("no")
        