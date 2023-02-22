# https://www.acmicpc.net/problem/2561


class ThreeFlipNumber:
    def __init__(self, N: int, arr: list):
        self.N = N
        self.arr = arr
        self._arr = self.arr.copy()
        self.sq_idx = []

    def is_sorted_numbers(self):
        for i in range(self.N):
            if self._arr[i] != i + 1:
                return False
        return True

    def sequence_check(self):
        is_sq = is_up = is_down = False
        i = si = ei = 0
        pre = -1
        while i < self.N:
            if not is_sq:
                if self._arr[i] != i+1:
                    si = ei = i
                    pre = self._arr[i]
                    is_sq = True

            else:
                if self._arr[i] == pre + 1:
                    if is_down:
                        self.sq_idx.append((si, ei))
                        si = ei = i
                        is_down = False
                        is_up = False
                    else:
                        is_up = True
                        ei = i
                elif self._arr[i] == pre - 1:
                    if is_up:
                        self.sq_idx.append((si, ei))
                        si = ei = i
                        is_up = False
                        is_down = False
                    else:
                        is_down = True
                        ei = i
                else:
                    self.sq_idx.append((si, ei))
                    si = ei = i
                    is_up = False
                    is_down = False
                pre = self._arr[i]
            i += 1
        if pre != i:
            self.sq_idx.append((si, ei))


    def find_flip_number(self):
        for i in range(self.N):
            if self._arr[i] != i+1:
                return i, self._arr.index(i+1)
        return 0, 0

    def reverse_find_flip_number(self):
        for i in range(self.N-1, -1, -1):
            if self._arr[i] != i+1:
                return self._arr.index(i+1), i
        return 0, 0

    def flip_numbers(self, index1, index2):
        self._arr[index1:index2+1] = self._arr[index1:index2+1][::-1]

    def solution(self):
        self.sequence_check()
        # print(self.sq_idx)
        orders = [(0, 1), (1, 0)]
        for i in range(len(self.sq_idx)):
            si = self.sq_idx[i][0]
            for j in range(i, len(self.sq_idx)):
                ei = self.sq_idx[j][1]
                self.flip_numbers(si, ei)
                ans1 = (si+1, ei+1)
                tmp_arr = self._arr.copy()

                # 정역, 역정
                # orders = [(0, 1), (1, 0)]
                for order in orders:
                    # print("=========", self.arr)
                    # print(order, tmp_arr, ans1)
                    ans2 = []
                    for p in order:
                        if p == 0:
                            flipped_number, index_number = self.find_flip_number()
                            self.flip_numbers(flipped_number, index_number)
                            ans2.append((flipped_number+1, index_number+1))
                        else:
                            index_number, flipped_number = self.reverse_find_flip_number()
                            self.flip_numbers(index_number, flipped_number)
                            ans2.append((index_number+1, flipped_number+1))
                        # print(order, self._arr, p, ans2)
                    if self.is_sorted_numbers():
                        print(*ans1)
                        for a in ans2:
                            print(*a)
                        # print(self._arr)
                        return
                    self._arr = tmp_arr

                self._arr = self.arr.copy()

if __name__ == "__main__":
    N = int(input().strip())
    arr = list(map(int, input().strip().split()))

    three_flip = ThreeFlipNumber(N, arr)
    three_flip.solution()