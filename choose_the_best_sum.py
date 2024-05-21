from itertools import combinations
def choose_best_sum(t,k,ls):
    
    possible_combinations = combinations(ls,k)
    
    best = 0
    for each in possible_combinations:
        if sum(each) <= t and sum(each) >= best:
            best = sum(each)
    return best        
        
    
choose_best_sum(163,3,[50, 55, 56, 57, 58])