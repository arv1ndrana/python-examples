list_of_names = ["Sita","Ram","Krishna", "Gita", "Dipendra", "Asha", "Rajendra"]

tuple_of_names = tuple(list_of_names)

list_of_names[1] = "Arvind"
tuple_of_names[1] = "Arvind" #Cause Error
# Because tuple is immutable or unchangable

print(list_of_names)
print(tuple_of_names)