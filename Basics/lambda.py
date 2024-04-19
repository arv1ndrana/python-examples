#Use lambda function only for temporary use

add = lambda x , y: x + y

cube = lambda x: x * x * x

print(add(1,2))
print(cube(4))


#NOT USEFUL
#Nested Function
def make_adder(n):
    return lambda x: x + n

plus_3 = make_adder(3)

print(plus_3(4))
