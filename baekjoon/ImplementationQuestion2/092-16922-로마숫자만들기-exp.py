# https://www.acmicpc.net/source/52717382

from itertools import combinations_with_replacement

print(len(set(sum(list(i)) for i in combinations_with_replacement([1,5,10,50], int(input())))))
