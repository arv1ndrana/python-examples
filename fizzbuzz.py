def solution(number):
    if number < 0:
        return 0
    Sum = 0
    for i in range(1,number):
        if (i % 3 == 0 and i % 5 == 0) or (i % 3 == 0) or (i % 5 == 0):
            Sum += i
    return Sum

for i in range(100):
    solution(i)
