// 메모리초과


const [T, ...arr] = require('fs').readFileSync('z.in').toString().trim().split('\n');


/** key(Character): a character of the string, data(String): the string, children(Object): next characters */
class Node {
    constructor(key, data=null) {
        this.key = key;
        this.data = data;
        this.children = {};
    }
}

/** Node Tree: insert(String): insert the string into tree, searchPrefix(String): check if the string is a prefix in the tree. */
class Trie {
    constructor(arr) {
        // this.insert = this.insert.bind(this);
        this.head = new Node(null);
        if (arr) {
            for (let i in arr) {
                this.insert(arr[i])
            }
        }
    }

    isEmpty(obj) {
        if (Object.entries(obj).length == 0) return true;
        else false;
    }

    insert(string) {
        let currNode = this.head;
        for (let i in string) {
            if (!currNode.children.hasOwnProperty(string[i])) {
                // console.log("currNode.children.hasOwnProperty=", string[i]);
                currNode.children[string[i]] = new Node(string[i]);
                // console.log("currNode.children:", currNode.children);
            }
            currNode = currNode.children[string[i]];
        }
        currNode.data = string;
    }

    searchPrefix(string) {
        let currNode = this.head;
        for (let i in string) {
            currNode = currNode.children[string[i]];
            // console.log("search_num:", string[i], "CUR_NODE", currNode)
        }
        if (!this.isEmpty(currNode.children)) return true;
        else return false;
    }
}

let result = "";
let s_idx = 0;
let e_idx = 0;
for (let i = 0; i < T; i++) {
    e_idx = s_idx + Number(arr[s_idx]);
    // console.log(s_idx, e_idx, arr[s_idx])
    const nums = arr.slice(s_idx+1, e_idx+1);
    nums.sort();
    const trie = new Trie(arr);
    // console.log("nums:", nums)
    let flag = false
    for (let n in nums) {
        // console.log("num:", nums[n])
        // console.log(trie)
        if (trie.searchPrefix(nums[n])) {
            flag = true;
            break;
        }
    }
    if (!flag) result += "YES\n";
    else result += "NO\n"
    s_idx = e_idx + 1;
}
console.log(result);