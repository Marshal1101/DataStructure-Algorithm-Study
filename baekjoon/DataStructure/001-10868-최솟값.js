const [nm, ...input] = require('fs').readFileSync('z.in').toString().trim().split('\n');
const [N, M] = nm.split(' ').map(Number);
const arr = new Array(N);
for (let i = 0; i < N; i++) {
    arr[i] = Number(input[i]);
}

const MAX = Number.MAX_SAFE_INTEGER;
const width = 2 ** Math.ceil(Math.log2(arr.length));
const tree = new Array(2 * width);

function initTree(start = 0, end = arr.length-1, node = 1) {
    if (start == end) {
        tree[node] = arr[start];
        return tree[node];
    }

    let mid = parseInt((start + end) / 2);
    let leftVal = initTree(start, mid, node * 2);
    let rightVal = initTree(mid+1, end, node * 2 + 1);
    tree[node] = leftVal < rightVal ? leftVal : rightVal;
    return tree[node];
}

function getMin(left, right, start = 0, end = arr.length-1, node = 1) {
    if (start > right || end < left) return MAX;
    if (left <= start && end <= right) return tree[node];

    let mid = parseInt((start + end) / 2);
    let leftVal = getMin(left, right, start, mid, node * 2);
    let rightVal = getMin(left, right, mid+1, end, node * 2 + 1);
    return leftVal < rightVal ? leftVal : rightVal;
}

initTree();

let a, b;
for (let i = N; i < N + M; i++) {
    [a, b] = input[i].split(' ').map(Number);
    console.log(getMin(a-1, b-1));
}