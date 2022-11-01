let s = require('fs').readFileSync('/dev/stdin').toString().trim().split('');
let a;
switch(s[0]) {
case 'A': a = 4.0; break;
case 'B': a = 3.0; break;
case 'C': a = 2.0; break;
case 'D': a = 1.0; break;
case 'F': a = 0.0; break;
}
if(a === 0.0) {
    console.log((0).toFixed(1));
}
else {
    switch(s[1]) {
    case '+': a += 0.3; break;
    case '-': a -= 0.3; break;
    }
    console.log(a.toFixed(1));
}