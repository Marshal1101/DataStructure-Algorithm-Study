from collections import defaultdict

def solution(clothes):
    
    dict = defaultdict(int)
    
    for set in clothes :
        cloth, kind = set
        dict[kind] += 1
    
    total = 1
    for value in dict.values() :
        total *= (value + 1)
    
    return total - 1