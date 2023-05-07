var fs = require('fs');
var input = fs.readFileSync('./dev/stdin').toString().split('\n');
var endl = '\n'
/* --- -- --- */

var a = BigInt(input[0]);
var b = BigInt(input[1]);

console.log((a+b)+endl+(a-b)+endl+(a*b));
