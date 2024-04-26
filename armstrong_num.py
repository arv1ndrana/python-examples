armstrong_numbers = []

for number in range(1,1000000000+1):
    string_number = str(number)
    string_number_len = len(string_number)

    _sum = 0
    for digit in string_number:
        _sum += int(digit) ** string_number_len

    if _sum == number:
        armstrong_numbers.append(number)

print(armstrong_numbers)
