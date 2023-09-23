import sys


class GoStack:
    def __init__(self, order: list = []) -> None:
        self.stk = []
        self.com = order
        self.is_error = False

    def order(self, order) -> None:
        self.com = order

    def exe(self, num: int) -> None:
        self.stk.clear()
        self.is_error = False
        self.stk.append(num)
        for i in range(len(self.com)):
            if self.com[i] == "POP":
                self.pop()
            elif self.com[i] == "INV":
                self.inv()
            elif self.com[i] == "DUP":
                self.dup()
            elif self.com[i] == "SWP":
                self.swp()
            elif self.com[i] == "ADD":
                self.add()
            elif self.com[i] == "SUB":
                self.sub()
            elif self.com[i] == "MUL":
                self.mul()
            elif self.com[i] == "DIV":
                self.div()
            elif self.com[i] == "MOD":
                self.mod()
            elif self.com[i] == "END":
                if len(self.stk) != 1 or abs(self.stk[0]) > 10**9:
                    self._error()
                else:
                    print(*self.stk)
            else:
                self.numx(self.com[i])
            if self.is_error:
                return


    def _error(self) -> None:
        self.is_error = True
        print("ERROR")
    
    def numx(self, nums) -> None:
        com, x = nums.split()
        self.stk.append(int(x))

    def pop(self) -> int:
        if len(self.stk) < 1:
            self._error()
            return
        return self.stk.pop()
    
    def inv(self) -> None:
        if len(self.stk) < 1:
            self._error()
            return
        self.stk[-1] = -self.stk[-1]
    
    def dup(self) -> None:
        if len(self.stk) < 1:
            self._error()
            return
        self.stk.append(self.stk[-1])

    def swp(self) -> None:
        if len(self.stk) < 2:
            self._error()
            return
        tmp1 = self.stk.pop()
        tmp2 = self.stk.pop()
        self.stk.append(tmp1)
        self.stk.append(tmp2)

    def add(self) -> None:
        if len(self.stk) < 2:
            self._error()
            return
        tmp1 = self.stk.pop()
        tmp2 = self.stk.pop()
        self.stk.append(tmp1 + tmp2)
    
    def sub(self) -> None:
        if len(self.stk) < 2:
            self._error()
            return
        tmp1 = self.stk.pop()
        tmp2 = self.stk.pop()
        self.stk.append(tmp2 - tmp1)

    def mul(self) -> None:
        if len(self.stk) < 2:
            self._error()
            return
        tmp1 = self.stk.pop()
        tmp2 = self.stk.pop()
        self.stk.append(tmp2 * tmp1)

    def div(self) -> None:
        if len(self.stk) < 2:
            self._error()
            return
        tmp1 = self.stk.pop()
        if tmp1 == 0:
            self._error()
            return
        flag = False
        if tmp1 < 0:
            flag = not flag
        tmp2 = self.stk.pop()
        if tmp2 < 0:
            flag = not flag
        if flag:
            ans = -(abs(tmp2) // abs(tmp1))
        else:
            ans = abs(tmp2) // abs(tmp1)
        self.stk.append(ans)

    def mod(self) -> None:
        if len(self.stk) < 2:
            self._error()
            return
        tmp1 = self.stk.pop()
        if tmp1 == 0:
            self._error()
            return
        flag = False
        tmp2 = self.stk.pop()
        if tmp2 < 0:
            flag = not flag
        if flag:
            ans = -(abs(tmp2) % abs(tmp1))
        else:
            ans = abs(tmp2) % abs(tmp1)
        self.stk.append(ans)


def main():
    input = sys.stdin.readline
    while True:
        gostk = GoStack()
        order = []
        while True:
            incom = input().rstrip()
            if incom == "QUIT":
                return
            elif incom == "":
                order.clear()
                print()
            else:
                order.append(incom)
            if incom == "END":
                break
        gostk.order(order)
        T = int(input())
        for _ in range(T):
            gostk.exe(int(input()))


if __name__ == '__main__':
    main()