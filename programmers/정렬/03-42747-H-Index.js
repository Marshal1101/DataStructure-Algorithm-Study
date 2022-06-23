function solution(citations) {
    var answer = 0;

    citations.sort((a, b) => a - b)
    end = citations.length
    lp = 0
    rp = citations.length - 1

    while (lp <= rp) {
        mid = parseInt((lp + rp) / 2)
        minUsed = citations[mid]
        papers = end - mid
        if (minUsed >= papers) {
            answer = papers > answer ? papers : answer        
            rp = mid - 1
        } else {
            answer = minUsed > answer ? minUsed : answer
            lp = mid + 1
        }
    }

    return answer;
}