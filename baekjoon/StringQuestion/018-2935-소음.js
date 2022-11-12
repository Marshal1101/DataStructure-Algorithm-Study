let [strA, opt, strB] = require('fs').readFileSync('z.in').toString().trim().split('\n');

let result, prefix;
if (opt == "+") {
    if (strA.length > strB.length) {
        prefix = strA.substring(0, (strA.length - strB.length));
        result = prefix + strB;
    }
    else if (strA.length == strB.length) {
        result = "2" + strA.substring(1, strA.length);
    }
    else {
        prefix = strB.substring(0, (strB.length - strA.length));
        result = prefix + strA;
    }
}
else {
    result = "1" + strA.substring(1, strA.length) + strB.substring(1, strB.length);
}

console.log(result);