function solution(progresses, speeds) {
    var answer = [];
    
    let ptr = 0;
    len = progresses.length
    while (ptr < len) {
        let cnt = 0;
        for (let i = ptr; i < len; i++) {
            cur_task = progresses[i]
            cur_speed = speeds[i]
            nex_task = cur_task + cur_speed;
            if (i == ptr && nex_task > 99) {
                cnt++;
                ptr++;
            }
            else progresses[i] = nex_task;
        }
        if (cnt) answer.push(cnt)
    }
    
    return answer;
}