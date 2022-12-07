import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

switch = False
while t:
    if t[-1] == 'A':
        t.pop()
    elif t[-1] == 'B':
        t.pop()
        t.reverse()
    if s == t:
        switch = True
        break

if switch:
    print(1)
else:
    print(0)


"""
문자열 S를 T로 바꾸는데 연산이 두 가지인데, 
이를 반대 관점에서 해석하여 문제를 풀려고 한다.

① S → T
문자열의 뒤에서 A를 추가한다.
문자열을 뒤집고 뒤에 B를 추가한다.


② T → S
문자열의 뒤에서 A를 제거한다.
문자열의 뒤에서 B를 제거하고 문자열을 뒤집는다.

① 관점에서 답을 구현하기 위해서는 문자열을 뒤집을지, 
문자열의 끝에 추가할지를 선택해야 한다. 
이 선택은 연산 횟수를 증가시켜 시간 복잡도를 높이는 결과를 초래한다. 
따라서 T를 S로 줄이는 과정을 문자열의 끝만을 확인하는 역연산(②)을 통해 
S를 T로 만들 수 있는지 없는지 알아낸다.
"""