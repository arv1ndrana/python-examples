def box(n):
    box = ['-' * n]

    for _ in range(n - 2):
        start = '-'
        for _ in range(n - 2):
            start += ' '
        start += '-'
        box.append(start)
    box.append('-' * n)

    return box

result = box(5)
print(result)
