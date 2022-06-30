function solution(people, limit) {
    people.sort(function(a, b){return a-b});
    for(var i=0, j=people.length-1; i < j; j--) {
        if( people[i] + people[j] <= limit ) i++;
    }    
    return people.length-i;
}

/*
정확성  테스트
테스트 1 〉	통과 (2.22ms, 31.8MB)
테스트 2 〉	통과 (1.11ms, 30MB)
테스트 3 〉	통과 (1.15ms, 30.1MB)
테스트 4 〉	통과 (1.11ms, 30MB)
테스트 5 〉	통과 (0.65ms, 29.9MB)
테스트 6 〉	통과 (0.39ms, 30MB)
테스트 7 〉	통과 (0.57ms, 30MB)
테스트 8 〉	통과 (0.12ms, 30MB)
테스트 9 〉	통과 (0.13ms, 30MB)
테스트 10 〉	통과 (1.06ms, 30MB)
테스트 11 〉	통과 (1.00ms, 30.2MB)
테스트 12 〉	통과 (0.85ms, 30.1MB)
테스트 13 〉	통과 (1.07ms, 30.1MB)
테스트 14 〉	통과 (1.29ms, 30.2MB)
테스트 15 〉	통과 (0.16ms, 30.3MB)
효율성  테스트
테스트 1 〉	통과 (15.13ms, 33.6MB)
테스트 2 〉	통과 (13.53ms, 33.6MB)
테스트 3 〉	통과 (14.42ms, 33.4MB)
테스트 4 〉	통과 (11.94ms, 33.7MB)
테스트 5 〉	통과 (12.05ms, 33.3MB)
*/