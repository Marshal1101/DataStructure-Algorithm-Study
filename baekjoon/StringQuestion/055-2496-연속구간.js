const input = require('fs').readFileSync('dev/stdin').toString().trim().split('\n');


for (const line of input) {
    let prev = "";
    let maxCnt = 1;
    let cnt = 1;
    for (let i = 0; i < line.length; i++) {
        if (line.charAt(i) == prev) {
            maxCnt = ++cnt > maxCnt ? cnt : maxCnt;
        }
            else {
            prev = line.charAt(i);
            cnt = 1;
        }
    }

    console.log(maxCnt);
}