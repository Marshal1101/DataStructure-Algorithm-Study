
from heapq import heappop, heappush, heapify
from collections import deque


opereation = ["I 7","I 5","I -5","D -1"]

num = []
for oper in opereation :
    oper.split(" ")
    if oper[0] == "I" :
        num.append(oper[1])
    elif oper[0] == "D" :
        heappop(num)



a = list(map(int, i for i in opereation))
print(a)
i = opereation.pop(-1)
if i == "D -1" :
    print(opereation[0])