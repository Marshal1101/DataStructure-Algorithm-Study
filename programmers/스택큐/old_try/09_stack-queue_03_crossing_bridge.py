## 스택, 큐 - 다리를 지나는 트럭 (구현)

from collections import deque

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

def solution(bridge_length, weight, truck_weights) :
    queue = deque(truck_weights)
    onbridge = deque([0] * bridge_length)
    time = 0
    waiting = deque([])
    total_weight = 0

    # 큐에 있거나 다리 위에 트럭이 있다면
    while queue or total_weight :
        try : 
            truck = queue.popleft()
            waiting.append(truck)
            # 트럭이 다리 앞에서 대기
            while waiting : 
                # 다리 위에 뭐든 일단 하나 내보내기
                passed_truck = onbridge.popleft()
                total_weight -= passed_truck
                # 무게 체크해서 가능하면 들여보내기
                if total_weight + truck <= weight :
                    allowed_truck = waiting.popleft()
                    onbridge.append(allowed_truck)
                    total_weight += allowed_truck
                # 초과면 계속 대기
                else :
                    onbridge.append(0)
                time += 1
        # 대기 없이 다리 위에 트럭들만 남았을 때,
        except :
            while total_weight > 0 :
                passed_truck = onbridge.popleft()
                onbridge.append(0)
                total_weight -= passed_truck
                time += 1
            
    return time

print(solution(bridge_length, weight, truck_weights))

