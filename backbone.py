import random

wrongletters = 0
listofwords = ["tree", "car", "nickel", "hangman", "penny"]
selectedword = random.choice(listofwords)
length = len(selectedword)
print("Your word has " + str(length) + " letters")
display = ("_ " * length)
print("Begin guessing letters")
while "_" in display and wrongletters < 6:
    userinput = input()
    if userinput in selectedword:
        print("You guessed a letter correctly, and you still have " + str(6 - wrongletters) + " guesses left!")
    elif userinput not in selectedword:
        print("You've guessed a letter incorrectly, and you have " + str(6 - wrongletters) + " guesses left!")
        wrongletters += 1
    print(display)

if wrongletters >= 6:
    print("You've ran out of guesses!")
