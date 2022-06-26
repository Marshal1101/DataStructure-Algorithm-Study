## 스택, 큐 - 기능개발 (구현)

progresses = [93, 30, 55]
speeds = [1, 30, 5]

def solution(progresses, speeds):
    answer = []
    # 리스트를 역순으로 하여 스택
    progresses.reverse()
    speeds.reverse()
    while progresses :
        for i in range(len(progresses)) :
            progresses[i] += speeds[i]
        cnt = 0
        # 가장 먼저 나와야할 연구가 100이 되어야만 pop
        while progresses and progresses[-1] >= 100 :
            progresses.pop()
            speeds.pop()
            cnt += 1
        if cnt > 0 :
            answer.append(cnt)            

    return answer

print(solution(progresses, speeds))