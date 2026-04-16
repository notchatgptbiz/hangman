import random

wrongletters = 0
listofwords = ["tree", "car", "nickel", "hangman", "penny"]
selectedword = random.choice(listofwords)
length = len(selectedword)
wrongguesses = 0
if length > 6:
    wrongguesses = 8
else:
    wrongguesses = 6
print("Your word has " + str(length) + " letters, and you have " + str(wrongguesses) + " guesses.")
display = ("_ " * length)
print("Begin guessing letters")
while "_" in display and wrongletters < wrongguesses:
    userinput = input()
    if userinput in selectedword:
        print("You guessed a letter correctly, and you still have " + str(wrongguesses - wrongletters) + " guesses left!")
    elif userinput not in selectedword:
        wrongletters += 1
        print("You've guessed a letter incorrectly, and you have " + str(wrongguesses - wrongletters) + " guesses left!")
    print(display)

if wrongletters >= wrongguesses:
    print("You've ran out of guesses!")
