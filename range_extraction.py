def solution(args):
    well_fuck = []
    shall_fuck = []
    for i, j in enumerate(args[:-1]):
        one = (abs(args[i]) - abs(args[i+1]) ==
               1) or (abs(args[i+1]) - abs(args[i]) == 1)
        if one:
            well_fuck.append(args[i])
            well_fuck.append(args[i+1])
        else:
            if not args[i] in well_fuck:
                shall_fuck.append(args[i])

    well_fuck = list(set(well_fuck))
    well_fuck = sorted(well_fuck)

    print(well_fuck)
    print(shall_fuck)

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4,
         5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
