def decimal_to_binary(number):
    binary = ""
    while number != 0:
        remainder = number % 2
        binary += str(remainder)
        number //= 2
    return int(binary[::-1])


result = decimal_to_binary(14)
print(result)
