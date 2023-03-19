N = int(input())

bin_N = ""
while N != 0:
    mod = N % 2
    bin_N += str(mod)
    N = N // 2

ans = 0
for i in range(len(bin_N)):
    ans += int(bin_N[i]) * 2 ** (len(bin_N)-1 - i)

print(ans)