const [meAh, docAh] = require('fs').readFileSync('dev/stdin').toString().trim().split('\n');
console.log(meAh.length >= docAh.length ? "go" : "no");