const [A, B] = require("fs").readFileSync("dev/stdin").toString().trim().split(" ");
const C = A - B;
console.log(C >= 0 ? C : -C);