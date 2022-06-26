function poll(arr, comp) {
    if (arr.length < 2) return arr.pop();

    const item = arr[0];
    arr[0] = arr.pop();

    let index = 0;
    let leftIndex = 2 * index + 1;
    let rightIndex = 2 * index + 2;

    while (leftIndex < arr.length) {
        const target = 
            rightIndex < arr.length &&
            comp(arr[rightIndex], arr[leftIndex])
                ? rightIndex
                : leftIndex;

        if (comp(arr[index], arr[target])) break;
        let temp = arr[target];
        arr[target] = arr[index];
        arr[index] = temp; 

        index = target;
        leftIndex = 2 * index + 1;
        rightIndex = 2 * index + 2;
    }

    return item;
}

function solution(operations) {
    let answer = []
    const maxH = []     // 최대힙
    const minH = []     // 최소힙
    let dict = new Map();       // 값 개수 카운팅

    operations.forEach((oper) => {
        
        const [order, num] = oper.split(" ");
        
        if (order === 'D') {
            while (num === '1' && maxH.length) {
                const _high = poll(maxH, (a, b) => b > a);
                const high = String(_high)
                if (dict.get(high) > 0) {
                    dict.set(high, dict.get(high)-1);
                    // console.log('D 1', _high, dict.get(high));
                    break;
                }
                
            }
            while (num === '-1' && minH.length) {
                const _low = poll(minH, (a, b) => a < b);
                const low = String(_low);
                if (dict.get(low) > 0) {
                    dict.set(low, dict.get(low)-1);
                    // console.log('D-1', _low, dict.get(low));
                    break;
                }                
            }
        }
        else {
            // 해당 숫자 카운트
            if (!dict.get(num)) dict.set(num, 1);
            else (dict.set(num, dict.get(num)+1));
            
            // 최대힙에 넣고 정렬
            let _num = Number(num);
            let index = maxH.push(_num) - 1;
            let parent = Math.floor((index-1) / 2);
            while (parent >= 0 && maxH[parent] < maxH[index]) {
                temp = maxH[parent];
                maxH[parent] = maxH[index];
                maxH[index] = temp;
                index = parent;
                parent = Math.floor((index-1) / 2);
            }
            // console.log('maxH', maxH);
            
            // 최소힙에 넣고 정렬
            index = minH.push(_num) - 1;
            parent = Math.floor((index-1) / 2);
            while (parent >= 0 && minH[parent] > minH[index]) {
                temp = minH[parent];
                minH[parent] = minH[index];
                minH[index] = temp;
                index = parent;
                parent = Math.floor((index-1) / 2);
            }
            // console.log('minH', minH);

        }
        
    })

    while (maxH.length) {
        const _high = poll(maxH, (a, b) => b > a);
        const high = String(_high)
        if (dict.get(high) > 0) {
            answer.push(_high);
            break;
        }            
    }
    if (answer.length < 1) answer.push(0);
    
    while (minH.length) {
        const _low = poll(minH, (a, b) => a < b);
        const low = String(_low)
        if (dict.get(low) > 0) {
            answer.push(_low);
            break;
        }            
    }
    if (answer.length < 2) answer.push(0);
    
    return answer;
}

console.log(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))