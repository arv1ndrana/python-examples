def rev_num(number):
    number = str(number)

    number = number[::-1]
    number = int(number)

    return number

print(rev_num(1000))
