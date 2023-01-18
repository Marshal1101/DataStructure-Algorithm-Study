import sys
from collections import deque


"""아이디어
1. easy) deque 사용
	deque 자체로 컨베이터 벨트 회전하듯
	값은 [내구도, 로봇여부] 리스트"""

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    queue = deque()
    for belt in map(int, input().split()):
        queue.append([belt, False])

    step = 0
    broken_belt = 0
    while broken_belt < K:  # 4. 내구도 0 개수 > K: 종료
        # 1. 벨트 회전
        queue.appendleft(queue.pop())
        # 1-1. 벨트 회전 후 로봇 내림
        if queue[N-1][1]:
            queue[N-1][1] = False

        # 2. 로봇 이동
        for i in range(N-2, -1, -1):
            if queue[i][1] and not queue[i+1][1] and queue[i+1][0] > 0:
                queue[i][1] = False
                queue[i+1][1] = True
                queue[i+1][0] -= 1
                if queue[i+1][0] == 0:
                    broken_belt += 1
        # 2-1. 로봇 이동 후 로봇 내림
        if queue[N-1][1]:
            queue[N-1][1] = False

        # 3. 올리는 위치에 로봇 올림
        if queue[0][0] > 0:
            queue[0][1] = True
            queue[0][0] -= 1
            if queue[0][0] == 0:
                broken_belt += 1

        step += 1

    print(step)


if __name__ == '__main__':
    main()