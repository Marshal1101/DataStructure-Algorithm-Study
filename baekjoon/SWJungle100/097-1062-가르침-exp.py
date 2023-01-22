# https://www.acmicpc.net/source/51523150


import sys
from itertools import combinations

input = sys.stdin.readline
n, k = map(int, input().split())
my_char = set(['a', 'n', 't', 'i', 'c'])

def anta_tica():
    if k<5: return 0
    
    candi_chars = set()
    word_list = []

    cnt = 0
    for _ in range(n):
        temp = set()
        temp.update(set((input().strip())) - my_char)

        if not temp: 
            cnt+=1
            continue

        if len(temp) <= k-5:
            word_list.append(temp)
            candi_chars.update(temp)

    if len(candi_chars) <= k-5:
        return cnt + len(word_list)

    max_cnt = 0
    for candi in combinations(candi_chars, k-5):
        candi = set(candi)
        temp_cnt = 0
        for word in word_list:
            if word <= candi:
                temp_cnt +=1
        max_cnt = temp_cnt if max_cnt < temp_cnt else max_cnt

    return max_cnt + cnt

print(anta_tica())


