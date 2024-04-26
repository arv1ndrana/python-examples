import random

languages = ["Python", "Javascript", "Brainfuck", "Lua", "Bash"]

language = random.choice(languages)
print(language)

length_of_blank = len(language)
blank = "_" * length_of_blank

while "_" in blank:
    guess = input("Enter a guess: ")
    if guess in language:
        for num, g in enumerate(language):
            if g == guess:
                blank = list(blank)
                blank[num] = g
        print("".join(blank))
