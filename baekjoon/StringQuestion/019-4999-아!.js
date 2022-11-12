const [meAh, docAh] = require('fs').readFileSync('z.in').toString().trim().split('\n');
console.log(meAh.length >= docAh.length ? "go" : "no");