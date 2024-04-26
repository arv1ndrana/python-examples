string = "Arvind Rana is the best"

string_list = string.split()
string_list_length = []
for i in string_list:
    string_list_length.append(len(i))
print(min(string_list_length))
