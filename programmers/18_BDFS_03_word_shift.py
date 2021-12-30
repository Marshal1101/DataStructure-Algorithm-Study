## 깊이/너비 우선 탐색(DFS/BFS) - 단어 변환

from collections import deque

begin = "hit"	
target = "cog"	
words = ["hot", "dot", "dog", "lot", "log", "cog"]	

def solution(begin, target, words):
    n = len(begin)
    queue = deque([(begin, 0)])
    while queue :
        now, changed_cnt = queue.popleft()
        for word in words :
            diff_alphabet = 0
            for i in range(n) :
                if now[i] != word[i] :
                    diff_alphabet += 1
            if diff_alphabet == 1 :
                if word == target :
                    return changed_cnt + 1
                else :
                    queue.append((word, changed_cnt+1))
    # targe으로 변환할 수 없으면 return 0
    return 0





