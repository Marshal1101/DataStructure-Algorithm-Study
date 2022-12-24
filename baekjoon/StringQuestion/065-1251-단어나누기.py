import sys

def permutation(string: str, start: int, end:int):
    
    ret = []
    stack = []
    for i in range(start+1, end-1):
        stack.append(string[start:i][::-1])
        for j in range(i+1, end):
            stack.append(string[i:j][::-1])
            stack.append(string[j:end][::-1])
            ret.append("".join(stack))
            stack.pop()
            stack.pop()
        stack.pop()

    print(len(ret))
    return ret

string = sys.stdin.readline().rstrip()
ans = permutation(string, 0, len(string))
ans.sort()
print(ans[0])


"""
1000자 498501 리스트
2000자 1997001 리스트
"""