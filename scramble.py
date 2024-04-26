def scramble(s1, s2):
    s2_set = set(s2)
    s2_list = list(s2_set)
    s2_list.sort()
    
    print(s2_list)

    for i in s2_list:
        print(s1.count(i))

scramble("hchozixiqmshpbb", "hbhcspbmc")
