def bfs(S):
    visited = set()
    qstack = [(1, 0)]
    time = 0
    while qstack:
        new_stack = []
        time += 1
        while qstack:
            disp, clip = qstack.pop()
            # 1. 화면 클립보드로 복사
            if (state := (disp, disp)) not in visited:
                new_stack.append(state)
                visited.add(state)
            # 2. 클립보드에서 화면으로 복사
            if (state := (disp+clip, clip)) not in visited:
                if state[0] == S: return time
                new_stack.append(state)
                visited.add(state)
            # 3. 화면에서 이모티콘 하나 삭제
            if disp-1 > 1 and (state := (disp-1, clip)) not in visited:
                if state[0] == S: return time
                new_stack.append(state)
                visited.add(state)
        qstack = new_stack

def main():
    S = int(input())
    print(bfs(S))


if __name__ == '__main__':
    main()