## 그래프 - 순위 ()

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

def solution(n, results) :
    winner_vs_idx = [[] for _ in range(n+1)]
    loser_vs_idx = [[] for _ in range(n+1)]
    for result in results :
        winner, loser = result
        winner_vs_idx[loser].append(winner)
        loser_vs_idx[winner].append(loser)

    idx_win_cnt = [0] * (n+1)
    idx_lose_cnt = [0] * (n+1)

    def count_up(i, list, cnt_list) :
        visited = [False] * (n+1)
        visited[i] = True
        stack = [i]
        while stack :
            idx = stack.pop()
            for vs in list[idx] :
                if not visited[vs] :
                    visited[vs] = True
                    cnt_list[vs] += 1
                    stack.append(vs)

    for i in range(1, n+1) :
        count_up(i, winner_vs_idx, idx_win_cnt)
        count_up(i, loser_vs_idx, idx_lose_cnt)

    result = 0
    for i in range(1, n+1) :
        if idx_win_cnt[i] + idx_lose_cnt[i] == n-1 :
            result += 1

    return result

print(solution(n, results))



# from collections import deque

# def solution(n, results):
#     answer = 0

#     win = [[] for _ in range(n+1)]
#     lose = [[] for _ in range(n+1)]

#     for result in results:
#         win[result[0]].append(result[1])
#         lose[result[1]].append(result[0])

#     for i in range(1,n+1):
#         visited = [False for _ in range(n+1)]
#         visited[0] = visited[i] = True
#         for nodes in [win, lose]:
#             dq = deque([i])
#             while dq:
#                 idx = dq.popleft()
#                 for node in nodes[idx]:
#                     if not visited[node]:
#                         visited[node] = True
#                         dq.append(node)
#         if False not in visited:
#             answer += 1
#     return answer