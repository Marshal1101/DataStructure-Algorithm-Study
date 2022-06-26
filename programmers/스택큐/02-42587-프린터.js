function solution(priorities, location) {
    var answer = 0;
    
    let labelPri = priorities.map((v, i) => [v, i]);
    // console.log(labelPri)
    
    let sortedPri = priorities.slice().sort((a, b) => b - a);
    // console.log(sortedPri)
    let i = 0
    let order = 0
    while (labelPri.length) {
        const [pri, idx] = labelPri.shift();
        // console.log(pri, idx)
        if (sortedPri[i] === pri) {
            order++;
            if (idx === location) return order;
            else i++;
        } else {
            labelPri.push([pri, idx])
        }
    }
    
    return answer;
}

console.log(solution([1, 1, 9, 1, 1, 1], 0))