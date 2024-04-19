def persistence(n):
    if len(str(n)) == 1:
        return 0
    else:
        result = 1
        while True:
            last_digit = n % 10
            result *= last_digit
            n = n // 10
            if n == 0:
                n = result
                if len(str(n)) == 1 and len(str(result)) == 1:
                    return result
                    break
                result = 1 


print(persistence(27))
