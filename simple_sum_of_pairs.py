def solve(number):
    string_number = str(number)
    list_number = [int(digit) for digit in string_number]
    sum_of_digits_of_number = sum(list_number)
    
    maximum_digit_sum = 0

    for first_number in range(1,number):
        second_number = number - first_number

        first_number_list = [int(digit) for digit in str(first_number)]
        second_number_list = [int(digit) for digit in str(second_number)]

        digit_sum = sum(first_number_list) + sum(second_number_list)

        if digit_sum > maximum_digit_sum:
            maximum_digit_sum = digit_sum

    return (maximum_digit_sum)
