## 스택 - 기능개발 ()

progresses = [93, 30, 55]
speeds = [1, 30, 5]

def solution(progresses, speeds):
    answer = []
    progresses.reverse()
    speeds.reverse()
    while progresses :
        for i in range(len(progresses)) :
            progresses[i] += speeds[i]
        cnt = 0
        while progresses and progresses[-1] >= 100 :
            progresses.pop()
            speeds.pop()
            cnt += 1
        if cnt > 0 :
            answer.append(cnt)            

    return answer

print(solution(progresses, speeds))