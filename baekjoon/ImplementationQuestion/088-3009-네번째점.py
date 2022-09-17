import sys


input = sys.stdin.readline
x_list = set()
y_list = set()
for _ in range(3) :
    x, y = map(int, input().split())
    if not x in x_list : x_list.add(x)
    else : x_list.remove(x)
    if not y in y_list : y_list.add(y)
    else : y_list.remove(y)

print(*x_list, end=" ")
print(*y_list)