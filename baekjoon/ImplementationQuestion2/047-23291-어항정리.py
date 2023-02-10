import sys


class Node():
    def __init__(self, key:int=None, val:int=None) -> None:
        self.key = key
        self.val = val
        self.adj = [set(), set()]


class Sol23291():
    def __init__(self, arr, K) -> None:
        if len(arr) < 4: return
        self.K = K
        self.N = len(arr)
        self.order = [*range(self.N)]
        self.nodes = [Node(i, v) for i, v in enumerate(arr)]
        self.head = 0
        self.tail = 0
        self.ptr = 1
        self.tick = 0
        self.max_val = 0
        self.min_val = sys.maxsize
        self.gap = None
        self.check()


    def travel(self, node, tick=None):
        if tick == None: tick = self.tick
        ans = []
        prev_key = node.key
        stk = [node]
        while stk:
            cur_node = stk.pop()
            ans.append(cur_node.key)
            for next_node in cur_node.adj[tick]:
                if next_node.key != prev_key:
                    stk.append(next_node)
            prev_key = cur_node.key
        return ans


    def add_fish(self):
        for key in self.order:
            if self.nodes[key].val == self.min_val:
                self.nodes[key].val += 1

    def stack1(self):
        stk_key = self.order[self.ptr-1]
        stk_node = self.nodes[stk_key]

        # 쌓인 어항이 더 길면, 바닥 어항들 가로방향 연결하고 종료
        if (h := len(self.travel(stk_node))) > (g := len(self.order) - self.ptr):
            self.tail = self.ptr
            # self.tick = not self.tick
            while self.ptr < len(self.order):
                ptr_key = self.order[self.ptr]
                ptr_node = self.nodes[ptr_key]
                stk_node.adj[not self.tick].add(ptr_node)
                stk_node = ptr_node
                self.ptr = self.ptr + 1
            return
        
        # 쌓인 어항이 더 굴러갈 수 있으면
        # 바닥 어항과 세로방향 연결
        self.head = self.ptr
        self.tick = not self.tick
        prev_key = set()
        prev_key.add(stk_key)
        stk = [stk_node]
        while stk:
            # 맞닿는 어항 연결
            cur_node = stk.pop()
            ptr_key = self.order[self.ptr]
            ptr_node = self.nodes[ptr_key]
            cur_node.adj[self.tick].add(ptr_node)
            ptr_node.adj[self.tick].add(cur_node)
            
            # 세로방향 다음 노드
            for next_node in cur_node.adj[not self.tick]:
                if next_node.key in prev_key: continue
                stk.append(next_node)
                prev_key.add(next_node.key)
                self.ptr = self.ptr + 1
        p = self.ptr
        self.ptr += 1
            
        # 바닥 어항끼리 연결
        p_node = self.nodes[self.order[p]]
        while p != self.head:
            np = p - 1
            npk = self.order[np]
            np_node = self.nodes[npk]
            p_node.adj[not self.tick].add(np_node)
            np_node.adj[not self.tick].add(p_node)
            p_node = np_node
            p -= 1

        if h == g:
            self.tail = self.ptr


    def stack2(self):
        self.tick = 0
        n = self.N
        mid = n // 2
        qurt = mid // 2
        self.tail = n
        self.head = (mid + self.tail) // 2

        for s in range(0, self.head+1, qurt):
            for i in range(s, s+qurt-1):
                node1 = self.nodes[self.order[i]]
                node2 = self.nodes[self.order[i+1]]
                node1.adj[self.tick].add(node2)
                node2.adj[self.tick].add(node1)


        self.tick = not self.tick
        rp = mid
        lp = rp-1
        while lp >= 0 and rp < n: 
            r_node = self.nodes[self.order[rp]]
            l_node = self.nodes[self.order[lp]]
            r_node.adj[self.tick].add(l_node)
            l_node.adj[self.tick].add(r_node)
            lp -= 1
            rp += 1

        rp = mid // 2
        lp = rp-1
        while lp >= 0 and rp < mid: 
            r_node = self.nodes[self.order[rp]]
            l_node = self.nodes[self.order[lp]]
            r_node.adj[self.tick].add(l_node)
            l_node.adj[self.tick].add(r_node)
            lp -= 1
            rp += 1


    def mix(self):
        temp = []
        visited = [False] * self.N
        for key in self.order:
            node = self.nodes[key]
            sub_vist = set()
            for i in range(2):
                for next in node.adj[i]:
                    if visited[next.key] or next.key in sub_vist: continue
                    sub_vist.add(next.key)
                    d = abs(node.val - next.val) // 5
                    if d > 0:
                        if node.val > next.val:
                            temp.append((node.key, -d))
                            temp.append((next.key, d))
                        else:
                            temp.append((next.key, -d))
                            temp.append((node.key, d))
            visited[key] = True

        for key, d in temp:
            self.nodes[key].val += d


    def check(self):
        min_val = sys.maxsize
        max_val = 0
        for key in self.order:
            if self.nodes[key].val < min_val:
                min_val = self.nodes[key].val
            if self.nodes[key].val > max_val:
                max_val = self.nodes[key].val
        self.gap = max_val - min_val
        self.min_val = min_val
        self.max_val = max_val


    def unfold(self):
        new_order = []
        p = self.head
        while p != self.tail:
            key = self.order[p]
            node = self.nodes[key]
            tr = self.travel(node)
            new_order.extend(tr)
            p += 1
        new_order.extend(self.order[self.tail:])
        self.order = new_order


    def adjclear(self):
        for node in self.nodes:
            node.adj[0].clear()
            node.adj[1].clear()


    def exe(self):
        count = 0
        while True:
            count += 1
            self.ptr = 1
            self.add_fish()
            while self.ptr < len(self.order):
                self.stack1()
            self.mix()
            self.unfold()
            self.adjclear()
            self.stack2()
            self.mix()
            self.check()
            self.unfold()
            self.adjclear()
            if self.gap <= self.K:
                return count


def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    line = list(map(int, input().split()))
    sol = Sol23291(line, K)
    print(sol.exe())


if __name__ == '__main__':
    main()