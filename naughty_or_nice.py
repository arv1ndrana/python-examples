def what_list_am_i_on(actions):
    naughty_letters = 'bfk'
    nice_letters= 'gsn'

    first_letters = [string[0] for string in actions]

    naughty = sum(1 for x in first_letters if x in naughty_letters)
    nice = sum(1 for x in first_letters if x in nice_letters)

    return 'naughty' if naughty >= nice else 'nice'

actions = ['broke someone\'s window', 'fought over a toaster', 'killed a bug']
result = what_list_am_i_on(actions)
print(result)
