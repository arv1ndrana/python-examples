def pig_it(text):time.py
    text_list = text.split()
    result = ""

    for phrase in text_list:
        if phrase.isalpha():
            first_letter = phrase[0]
            phrase = phrase[1:]

            result += f"{phrase}{first_letter}ay "
        else:
            result += f"{phrase} "

    return result[:-1]

print(pig_it("Hi ! MOM"))
