import sys


class ThreeTimes:
    def __init__(self, N) -> None:
        self.arr = [*range(N+1)]


    def part_reverse(self, si, ei):
        pre = self.arr[:si]
        suf = self.arr[ei+1:]
        tmp = self.arr[si:ei+1]
        tmp.reverse()
        self.arr = pre + tmp + suf

    def out(self):
        print(self.arr)


def main():
    input = sys.stdin.readline
    N = int(input())
    tt = ThreeTimes(N)

    tt.part_reverse(3, 8)
    tt.part_reverse(1, 5)
    tt.part_reverse(6, 9)
    tt.out()

    
    tt.part_reverse(6, 9)
    tt.out()
    tt.part_reverse(1, 5)
    tt.out()
    tt.part_reverse(3, 8)
    tt.out()


if __name__ == '__main__':
    main()