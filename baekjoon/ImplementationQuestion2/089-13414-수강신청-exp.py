import sys

def solution():
    K, L = map(int, input().split())
    temp = sys.stdin.readlines()
    students = dict()
    success = []
    for i in range(L-1, -1, -1):
        student = temp[i].rstrip()
        if students.get(student, 0):
            continue
        students[student] = 1
        success.append(student)
    print('\n'.join(success[::-1][:K]))

solution()