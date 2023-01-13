# Lv 2.
# https://school.programmers.co.kr/learn/courses/30/lessons/86971


#1 bfs
from collections import deque

def bfs_cnt(n, start, banned, graph):
    visited = [False for _ in range(n+1)]
    
    cnt = 0
    queue = deque([start])
    visited[start] = True
    visited[banned] = True
    while queue:
        node = queue.popleft()
        cnt += 1
        for next in graph[node]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                
    return cnt

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    for wire in wires:
        v1, v2 = wire
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    for cut in wires:
        v1, v2 = cut
        cnt1 = bfs_cnt(n, v1, v2, graph)
        cnt2 = n - cnt1
        diff = abs(cnt1 - cnt2)
        if diff < answer: answer = diff
        
    return answer


#2 union-find
def find(a):
    global uf
    if uf[a] < 0: return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)
    if pa == pb: return
    uf[pa] += uf[pb]
    uf[pb] = pa

def solution(n, wires):
    global uf
    answer = int(1e9)
    k = len(wires)
    for i in range(k):
        uf = [-1 for _ in range(n+1)]
        tmp = [wires[x] for x in range(k) if x != i]
        for a, b in tmp: merge(a, b)
        v = [x for x in uf[1:] if x < 0]
        answer = min(answer, abs(v[0]-v[1]))

    return answer


#3 set, list comprehension
def solution(n, wires):
    ans = n
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
        s = set(sub[0])
        [s.update(v) for _ in sub for v in sub if set(v) & s]
        ans = min(ans, abs(2 * len(s) - n))
    return ans