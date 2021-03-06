// https://www.acmicpc.net/source/27030854

const fs = require("fs");
const input = fs.readFileSync("/dev/stdin", "utf8").trim().split("\n");

function solution(preOrder) {
    const postOrder = [];
    const stack = [[0, preOrder.length - 1]];

    while (stack.length > 0) {
        const [start, end] = stack.pop();

        if (start > end) continue;
        postOrder[postOrder.length] = preOrder[start];

        let index = -1;

        for (let i = start + 1; i <= end; i += 1) {
            if (preOrder[start] < preOrder[i]) {
                index = i;
                break;
            }
        }

        if (index > 0) {
            stack[stack.length] = [start + 1, index - 1];
            stack[stack.length] = [index, end];
        } else {
            stack[stack.length] = [start + 1, end];
        }
    }

    return postOrder.reverse().join("\n");
}

const preOrder = input.map(Number);
const ans = solution(preOrder);

console.log(ans);