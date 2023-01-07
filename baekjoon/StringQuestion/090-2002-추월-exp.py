import sys
IN = []
OUT = []
N = int(sys.stdin.readline())

for i in range(N):
    IN.append(sys.stdin.readline().strip())
for i in range(N):
    OUT.append(sys.stdin.readline().strip())

count = 0
target = N - 1

while(IN != OUT):
    if OUT[target] != IN[target] :
        tmp = IN[target]
        OUT.remove(tmp)
        OUT.insert(target,tmp)
        count += 1
    target -= 1

print(count)