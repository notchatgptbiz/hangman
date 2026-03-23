import random

userinput = input("Guess a letter")
print(userinput)
listofwords = ["tree", "car", "nickel", "hangman", "penny"]
selectedword = random.choice(listofwords)
length = len(selectedword)
if userinput in selectedword:
  print("You guessed a letter correctly!")
else:
  print("You've guessed a letter incorrectly!")

print(length)
