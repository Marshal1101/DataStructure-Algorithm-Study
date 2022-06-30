def solution(routes):
    answer = 0
    camera = -30001
    
    routes.sort(key = lambda x:x[1])
    
    for start, end in routes:
        if start>camera:
            camera = end
            answer+=1
            
    return answer
