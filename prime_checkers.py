def prime_checker(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

result = prime_checker(11)
print(result)
