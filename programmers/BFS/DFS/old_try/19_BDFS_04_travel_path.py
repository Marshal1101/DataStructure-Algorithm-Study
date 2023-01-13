# 깊이/너비 우선 탐색(DFS/BFS) 여행경로 (참조)

from collections import defaultdict

def solution(tickets):
    answer = []
    routes = defaultdict(list)

    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])

    for key in routes.keys():
        routes[key].sort(reverse=True)

    stack = ['ICN']
    while stack:
        tmp = stack[-1]

        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())
    answer.reverse()

    return answer



## (참조: 승현)
from collections import defaultdict 

def solution(tickets): 
    answer = [] 
    graph = defaultdict(list) 
    
    for start, end in sorted(tickets): 
        graph[start].append(end) 
    
    def DFS(start): 
        while graph[start]:
            DFS(graph[start].pop(0)) 
        answer.append(start)

    DFS('ICN') 
    
    answer.reverse()
    return answer 