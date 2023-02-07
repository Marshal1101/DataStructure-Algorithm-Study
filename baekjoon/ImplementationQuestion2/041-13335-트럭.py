import sys
from collections import deque


def main():
    input = sys.stdin.readline
    N, W, L = map(int, input().split())
    bridge = deque([0 for _ in range(W)])
    truck = deque(list(map(int, input().split())))

    # 트럭이 다리 위에 올라갈 수 있는가?
    time = 0
    t_cnt_on = 0
    while truck:
        time += 1
        to = bridge.popleft()
        if to > 0:
            L += to
            t_cnt_on -= 1
        if truck[0] <= L:
            L -= truck[0]
            bridge.append(truck.popleft())
            t_cnt_on += 1
        else:
            bridge.append(0)

    while t_cnt_on > 0:
        time += 1
        to = bridge.popleft()
        if to > 0:
            t_cnt_on -= 1
    
    print(time)


if __name__ == '__main__':
    main()