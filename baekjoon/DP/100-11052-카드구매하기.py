N = int(input())
mem = [0] + [*map(int, input().split())]
for i in range(2, N+1):
    for j in range(1, i):
        mem[i] = max(mem[i], mem[i-j] + mem[j])

print(mem[-1])