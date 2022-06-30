import collections

def solution(name):
    def get_index(idx, d, L) :
        new_idx = idx + d
        if new_idx == -1 : new_idx = L - 1
        elif new_idx == L : new_idx = 0
        return new_idx

    def get_updown(a) :
        res = 0
        a_ascii = ord(a)
        if a_ascii < 78 : res = a_ascii - 65
        elif a_ascii > 78 : res = 91 - a_ascii
        else : res = 13
        return res

    def get_move_cnt(clist, L, step) :
        path = []
        cnt = 0
        if clist[0] :
            path.append(0)
            cnt += 1
        que = collections.deque([(0, cnt, 0, path)])
        move = 0
        while que :
            length = len(que)

            for _ in range(length) :
                idx, cnt, dir, path = que.popleft()
                if cnt == step : 
                    return move

                if clist[idx] or dir == 0 :
                    for d in (-1, 1) :
                        new_idx = get_index(idx, d, L)
                        if not clist[new_idx] or new_idx in path :
                            que.append((new_idx, cnt, d, path[:])) 
                        else :
                            path.append(new_idx)
                            que.append((new_idx, cnt+1, d, path[:]))
                            path.pop()
                else :
                    new_idx = get_index(idx, dir, L)                    
                    if not clist[new_idx] or new_idx in path :
                        que.append((new_idx, cnt, dir, path[:]))
                    else : 
                        path.append(new_idx)
                        que.append((new_idx, cnt+1, dir, path[:]))
                        path.pop()

            move += 1

    if (L := len(name)) == 1 : 
        return get_updown(name[0])
    else :
        ans = 0
        cnt = 0
        checklist = [False] * L
        for i in range(L) :
            if name[i] != "A" :
                ans += get_updown(name[i])
                cnt += 1
                checklist[i] = True

        ans += get_move_cnt(checklist, L, cnt)

    return ans