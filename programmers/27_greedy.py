def solution(number, k):
    answer = [] # Stack
    
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
        
    return ''.join(answer[:len(answer) - k])


print(solution("8", 0))
print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("4177252841", 8))
print(solution("12345678901234567890", 19))