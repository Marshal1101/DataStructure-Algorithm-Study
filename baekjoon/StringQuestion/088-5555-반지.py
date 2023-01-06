import sys


def bf_search(src, search):
    begin = 0
    while begin < len(src):
        is_match = True
        for i in range(len(search)):
            if src[(begin+i)%10] != search[i]:
                is_match = False
                begin += 1
                break
        if is_match: return True
    
    return False


input = sys.stdin.readline
search = input().rstrip()
N = int(input())
cnt = 0
for i in range(N):
    if (bf_search(input().rstrip(), search)):
        cnt += 1

print(cnt)