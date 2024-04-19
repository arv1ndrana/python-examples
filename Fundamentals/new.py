def generate_self_descriptive():
    for num in range(1_000_000_000, 10_000_000_000):
        digits = [int(d) for d in str(num)]
        count = [0] * 10

        for digit in digits:
            if digit >= 10:
                continue
            count[digit] += 1

        if count == digits:
            return num
            break

self_descriptive_number = generate_self_descriptive()
print(self_descriptive_number)

