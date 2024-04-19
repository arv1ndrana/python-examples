number = int(input("Enter a number: ")) 
factor = 0
factor_list = []

for i in range(1, number + 1):
    if number % i == 0:
        factor += 1
        factor_list.append(i)
    else:
        continue

if factor == 0 or factor == 1:
    print(str(number) + "is neither prime number nor composite number.")
elif factor >= 2:
    print(str(number) + " is a prime number.")
else:
    print(str(number) + " is a composite number.")

print(f"As, it has {factor} no. of factors which are")
print(factor_list)
