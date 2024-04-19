#number = [i for i in range(1,7)]
#print(number)
#
#new_list = [num * 2 if num % 2 == 0 else num for num in number]
#print(new_list)

foo = {"abs", "biceps"}
foo = {bar.upper() for bar in foo}

print(foo)

eggs = {"name": "Arvind", "age": 15}
eggs = {spam: k for k, spam in eggs.items()}
print(eggs)

c = {"name":"Arvind", "age":15 }
c_list = [f"{k.upper()}{v}" for k, v in c.items()]

print(c_list)
