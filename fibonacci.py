#!/usr/bin/python

def fibonacci(terms):
    num = 1
    fibonacci_list = [0, 1, 1]
    for num in range(2, terms + 1):
        number = (num - 1) + (num + 2)
        fibonacci_list.append(number)
    print(fibonacci_list)

fibonacci(10)
