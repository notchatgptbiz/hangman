import random

listofwords = ["tree", "car", "nickel", "hangman", "penny"]
selectedword = random.choice(listofwords)
length = len(selectedword)
print("Your word has " + str(length) + " letters")
display = ("_ " * length)
print("Begin guessing letters")
while "_" in display:
    userinput = input()
    if userinput in selectedword:
        print("You guessed a letter correctly!")
    elif userinput not in selectedword:
        print("You've guessed a letter incorrectly!")
    print(display)
