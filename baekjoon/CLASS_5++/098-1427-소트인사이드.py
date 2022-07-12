import sys

string = list(sys.stdin.readline().rstrip())
string.sort(reverse=True)
print(''.join(string))