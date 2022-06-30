## 정렬 - 가장 큰 수 (참조)

numbers = [3, 30, 34, 5, 9]

def solution(numbers):
    answer = ''
    numbers_str = list(map(str, numbers))
    numbers_str.sort(reverse=True, key=lambda x: x*3)
    answer += str(int(''.join(numbers_str)))
    return answer

print(solution(numbers))