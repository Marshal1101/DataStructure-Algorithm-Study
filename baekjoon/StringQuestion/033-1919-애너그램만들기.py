import sys


input = sys.stdin.readline

alphabet = [0 for _ in range(26)]
for i in input().rstrip():
    alphabet[ord(i)-97] += 1
for i in input().rstrip():
    alphabet[ord(i)-97] -= 1

delCnt = 0
for cnt in alphabet:
    delCnt += cnt if cnt >= 0 else -cnt

print(delCnt)