function solution(array, commands) {
    var answer = [];
    
    len = commands.length;
    for (let z = 0; z < len; z++) {
        const [i, j, k] = commands[z];
        cutArray = array.slice(i-1, j).map(Number).sort((a, b) => a - b)
        answer.push(cutArray[k-1])
    }
    
    return answer;
}