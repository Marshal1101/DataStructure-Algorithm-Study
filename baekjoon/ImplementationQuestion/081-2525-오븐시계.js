const input = require("fs").readFileSync("z.in").toString().trim().split("\n");

const startTime = input[0].split(' ').map(Number);
const workMinute = Number(input[1]);

const tempMinute = startTime[1] + workMinute;
let h = startTime[0] + parseInt(tempMinute / 60);
if (h > 23) h = h - 24;
let m = tempMinute % 60;

console.log(h + " " + m)