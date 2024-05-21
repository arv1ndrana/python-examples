original = [ 1, [ 1, 1 ] ]
other = [ 2, [ 2, 2 ] ] 
def same_structure_as(original, other):
    for i,j in zip(original, other):
        if type(i) == type(j):
            if isinstance(i,list) and isinstance(j,list):
                same_structure_as(i,j)
            if not original.index(i) == other.index(j):
                return False
        else:
            return False
        return True

print(same_structure_as(original,other))
