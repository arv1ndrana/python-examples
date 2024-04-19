#!/usr/bin/env python
word = "BOOM"

length = len(word)
blank = "_" * length
blank = list(blank)
while "_" in blank:
    guess = input("Enter your guess [Press <C-c> to exit]: ")

    if guess in word:
        for i, j in enumerate(word):
            if j == guess:
                blank[i] = guess
    else:
        print("Guess not correct")
    print("".join(blank))
