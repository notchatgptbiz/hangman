import random

listofwords = ["tree", "car", "nickel", "hangman", "penny"]
selectedword = random.choice(listofwords)
length = len(selectedword)
print("Your word has " + str(length) + " letters")
display = ("_" * length)
while "_" in display:
    print("Begin guessing letters")
    userinput = input()
    if userinput == " " or "" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0" or "-" or "+" or "_" or "=" or "," or "." or "?" or "/" or "!" or "@" or "#" or "$" or "%" or "^" or "&" or "*" or "(" or ")" or ":" or ";" or "{" or "}" or "[" or "]" or "|" or "<" or ">" or "`" or "~":
        print("You've guessed: \"" + userinput + "\", which is an invalid response. Remember to only guess letters")
    elif userinput in selectedword:
        print("You guessed a letter correctly!")
    else:
        print("You've guessed a letter incorrectly!")
    print(display)
