const [T, ...arr] = require('fs').readFileSync('z.in').toString().trim().split('\n');

const hasThisFromTheFirst = (src, search) => {
    const leng = src.length < search.length ? src.length : search.length;

    for (let i = 0; i < leng; i++) {
        if (src[i] != search[i]) return false;
    }

    return true;
}

let result = [];
let s_idx = 0;
let e_idx = 0;
let N_idx = 0;
for (let i = 0; i < T; i++) {
    e_idx = N_idx + arr[N_idx];
    s_idx = N_idx + 1
    let flag = false
    for (let j = s_idx; j <= e_idx; j++) {
        if (flag) break;
        for (let k = j; k > s_idx; k--) {
            if (hasThisFromTheFirst(arr[j], arr[k])) {
                result.push("NO");
                flag = true;
                break;
            }
        }
    }
    if (!flag) result.push("YES");
    N_idx += e_idx + 1;
}

console.log(result.join('\n'));