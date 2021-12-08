## 정렬 - K 번째 수 (구현)

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for com in commands:
        i, j, k = com
        tmp = array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])    
    return answer

print(solution(array, commands))