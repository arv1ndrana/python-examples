def maximum(array):
    maximum = 0
    for number in array:
        if number > maximum:
            maximum = number
    return maximum
