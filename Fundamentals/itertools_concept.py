import itertools

string = "hhaappyy bbiirrtthhddaayy"
string = string.replace(" ", "")

string_length = len(string)
string_list = []

for i in range(1, string_length+1):
    what = itertools.combinations(string, i)
    for i in what:
        i_string = "".join(i)
        string_list.append(i_string)

happy_count = string_list.count('happy')
birthday_count = string_list.count('birthday')

print(min(happy_count, birthday_count))
