def solution(name):
    if set(name) == {'A'}:
        return 0

    answer = float('inf')
    for i in range(len(name) // 2): # 반 이상 움직일 필요 없음
        left_moved = name[-i:]+name[:-i]
        right_moved = name[i:]+name[:i]
        print('-a-')
        print(left_moved)
        print(right_moved)
        print('-b-')
        for n in [left_moved, right_moved[0]+right_moved[:0:-1]]:
            print(n)
            while n and n[-1] == 'A':
                n = n[:-1]
            row_move = i + len(n)-1
            col_move = 0
            for c in map(ord, n):
                col_move += min(c - 65, 91 - c)

            answer = min(answer, row_move + col_move)

    return answer


"""
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.05ms, 10.3MB)
테스트 5 〉	통과 (0.05ms, 10.1MB)
테스트 6 〉	통과 (0.03ms, 10.4MB)
테스트 7 〉	통과 (0.08ms, 10.2MB)
테스트 8 〉	통과 (0.02ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.2MB)
테스트 10 〉	통과 (0.04ms, 10.2MB)
테스트 11 〉	통과 (0.05ms, 10.2MB)
테스트 12 〉	통과 (0.05ms, 10.2MB)
테스트 13 〉	통과 (0.16ms, 10.2MB)
테스트 14 〉	통과 (0.07ms, 10.4MB)
테스트 15 〉	통과 (0.09ms, 10.2MB)
테스트 16 〉	통과 (0.00ms, 10.1MB)
테스트 17 〉	통과 (0.00ms, 10.4MB)
테스트 18 〉	통과 (0.08ms, 10.2MB)
테스트 19 〉	통과 (0.03ms, 10.4MB)
테스트 20 〉	통과 (0.08ms, 10.2MB)
테스트 21 〉	통과 (0.03ms, 10.4MB)
테스트 22 〉	통과 (0.08ms, 10.4MB)
테스트 23 〉	통과 (0.04ms, 10.2MB)
테스트 24 〉	통과 (0.03ms, 10.3MB)
테스트 25 〉	통과 (0.09ms, 10.2MB)
테스트 26 〉	통과 (0.04ms, 10.3MB)
테스트 27 〉	통과 (0.04ms, 10.2MB)
"""