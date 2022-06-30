function solution(people, limit) {
    var answer = 0;
    
    people.sort((a, b) => b - a);
    ptr = 0;
    while (people.length > ptr) {
        let spare = limit;
        
        // 큰 사람 체크
        while (people.length > ptr) {
            if (people[ptr] <= spare) {
                spare -= people[ptr++];
            } else break;
        }
        // 작은 사람 체크
        while (people.length) {
            if (people[people.length-1] <= spare) {
                spare -= people.pop()
            } else break;            
        }
        // 배사용 증가
        answer++;
    }
    
    return answer;
}

/*
정확성  테스트
테스트 1 〉	통과 (2.66ms, 31.7MB)
테스트 2 〉	통과 (1.41ms, 29.8MB)
테스트 3 〉	통과 (1.48ms, 30.2MB)
테스트 4 〉	통과 (1.44ms, 29.9MB)
테스트 5 〉	통과 (0.88ms, 30MB)
테스트 6 〉	통과 (0.54ms, 30MB)
테스트 7 〉	통과 (0.79ms, 30.1MB)
테스트 8 〉	통과 (0.17ms, 29.9MB)
테스트 9 〉	통과 (0.22ms, 29.8MB)
테스트 10 〉	통과 (1.43ms, 30MB)
테스트 11 〉	통과 (1.18ms, 30.1MB)
테스트 12 〉	통과 (1.06ms, 30.1MB)
테스트 13 〉	통과 (1.46ms, 29.9MB)
테스트 14 〉	통과 (1.68ms, 30MB)
테스트 15 〉	통과 (0.25ms, 30MB)
효율성  테스트
테스트 1 〉	통과 (40.22ms, 33.2MB)
테스트 2 〉	통과 (35.75ms, 33.2MB)
테스트 3 〉	통과 (38.42ms, 33.2MB)
테스트 4 〉	통과 (27.09ms, 33.3MB)
테스트 5 〉	통과 (34.51ms, 33.1MB)
*/