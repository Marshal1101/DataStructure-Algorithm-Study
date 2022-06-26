
```js
// 2x2 매트릭스 생성
let dp = Array.from({ length: lenY }, () => new Array(lenX).fill(0));
```


```js
// 힙(comp), comp = (a, b) => a > b, 또는 a < b
class Heap {
    constructor(comp) {
        this.items = [];
        this.comp = comp;
    }

    get size() {
        return this.items.length;
    }

    swap(a, b) {
        const temp = this.items[a];
        this.items[a] = this.items[b];
        this.items[b] = temp;
    }

    getParentIndex(index) {
        return Math.floor((index - 1) / 2);
    }

    getLeftChildIndex(index) {
        return index * 2 + 1;
    }

    getRightChildIndex(index) {
        return index * 2 + 2;
    }

    peak() {
        return this.items[0];
    }

    add(item) {
        // push()는 배열 길이를 반환한다.
        let index = this.items.push(item) - 1;
        let parentIndex = this.getParentIndex(index);

        while (
            parentIndex >= 0 &&
            this.comp(this.items[index], this.items[parentIndex])
        ) {
            this.swap(index, parentIndex);
            index = parentIndex;
            parentIndex = this.getParentIndex(index);
        }
    }

    poll() {
        if (this.size < 2) return this.items.pop();

        const item = this.peak();
        this.items[0] = this.items.pop();

        let index = 0;
        let leftIndex = this.getLeftChildIndex(index);      // 2*idx + 1
        let rightIndex = this.getRightChildIndex(index);    // 2*idx + 2

        while (leftIndex < this.size) {
            const target =
                rightIndex < this.size &&
                    this.comp(this.items[leftIndex], this.items[rightIndex])
                    ? leftIndex
                    : rightIndex;

            if (this.comp(this.items[index], this.items[target])) break;
            this.swap(index, target);

            index = target;
            leftIndex = this.getLeftChildIndex(index);
            rightIndex = this.getRightChildIndex(index);
        }

        return item;
    }
}
```