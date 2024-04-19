def min(arr):
    low = arr[0]
    for i in arr[1:]:
        if i < low:
            low = i
    return low

def max(arr):
    high = arr[0]
    for i in arr[1:]:
        if i > high:
            high = i
    return high

random_array = [797, 910, 993, 707, 907, 508, 407, 642, 316, 244, 140, 393, 578, 307, 736, 603, 669, 451, 800, 334, 346, 548, 314, 125, 890, 406, 329, 335, 101, 390, 927, 630, 884, 679, 100, 423, 824]

print(min(random_array))
print(max(random_array))

