const [N, ...input] = require('fs').readFileSync('dev/stdin').toString().trim().split('\n');


for (let i = 0; i < input.length; i++) {
    console.log('%d\. %s', i+1, input[i]);
}