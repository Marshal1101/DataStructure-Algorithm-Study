const [N, ...arr] = require('fs').readFileSync('z.in').toString().trim().split('\n');


const map = new Map();
let curBook, cnt, maxSellBook, maxSellCnt = 0;
for (let i = 0; i < N; i++) {
    curBook = arr[i];
    if (map.has(curBook)) {
        cnt = map.get(curBook);
        map.set(curBook, ++cnt);
    }
    else {
        map.set(curBook, 1);
    }

    if (map.get(curBook) > maxSellCnt) {
        maxSellCnt = map.get(curBook);
        maxSellBook = curBook;
    }
    else if (map.get(curBook) == maxSellCnt && curBook != maxSellBook) {
        maxSellBook = (curBook < maxSellBook ? curBook : maxSellBook);
        // console.log("in")
        // const tmp = [curBook, maxSellBook];
        // tmp.sort();
        // console.log(tmp)
        // maxSellBook = tmp[0];
    }
}
console.log(maxSellBook);