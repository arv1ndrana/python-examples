input_number = input("Enter a number: ")

string_input_number = str(input_number)

sum_of_digits = 0

for digit in string_input_number:
    sum_of_digits += int(digit)

print(sum_of_digits)
