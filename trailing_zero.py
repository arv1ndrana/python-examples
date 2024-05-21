def zeros(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1

    result_string = str(result)
    result_string_strip = result_string.strip("0")

    return len(result_string) - len(result_string_strip)
    

    
print(zeros(12))
