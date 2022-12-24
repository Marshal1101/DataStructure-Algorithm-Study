import sys


def pelindrome(string: str, s_idx: int, e_idx: int) -> bool:
    while (s_idx <= e_idx):
        if string[s_idx] != string[e_idx]:
            return False
        s_idx += 1
        e_idx -= 1
    return True

string = sys.stdin.readline().rstrip()
min_len = len(string) * 2 - 1
for c in range(1, len(string)+1):
    e_idx = len(string) - 1
    s_idx = len(string) - c
    if pelindrome(string, s_idx, e_idx):
        min_len = len(string) + s_idx

print(min_len)