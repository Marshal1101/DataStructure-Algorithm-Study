def solution(n, lost, reserve):
    answer = n
    
    lost_set = set(lost)
    reserve_set = set(reserve)
    for i in lost :
        if i in reserve_set :
            reserve_set.discard(i)
            lost_set.discard(i)
            
    new_list = list(lost_set)
    new_list.sort()
    for i in new_list :
        if i-1 in reserve_set :
            reserve_set.discard(i-1)
        elif i+1 in reserve_set :
            reserve_set.discard(i+1)
        else :
            answer -= 1
                
    return answer