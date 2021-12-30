# 깊이/너비 우선 탐색(DFS/BFS) 여행경로 ()
from collections import deque
from heapq import heappop, heappush

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

# [['ATL', 'ICN'], ['ATL', 'SFO'], ['ICN', 'ATL'], ['ICN', 'SFO'], ['SFO', 'ATL']]

def solution(tickets):
    n = len(tickets)
    start = tickets[0][0]
    tickets.sort()
    for i in range(n) :
        if tickets[i][0] == start :
            visited = [False] * n
            path_list = [start]
            path_cnt = 0
            visited[i] = True
            visited_cnt = 1
            stack = [tickets[i]]        
            while stack :
                used_ticket = stack.pop()
                path_list.append(used_ticket[1])
                path_cnt += 1
                if path_cnt == n:
                    return path_list
                elif path_cnt > n :
                    break
                if visited_cnt <= n :
                    for j in range(n-1, -1, -1) :
                        if tickets[j][0] == used_ticket[1] :
                            if not visited[j] :
                                visited[j] = True
                                visited_cnt += 1
                                stack.append(tickets[j])