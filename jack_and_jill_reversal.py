def solve(n,k):    
    List = [num for num in range(0,n)]
    final_list = []

    for i in List:
        List = List[::-1]
        final_list.append(List[0])
        List = List[1:]
    return final_list.index(k)

print(solve(4,3))
