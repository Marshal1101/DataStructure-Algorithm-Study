# https://www.acmicpc.net/source/55320916

# 백준 - 두 번 뒤집기

## 문제
# 1부터 N까지의 숫자 오름차순 정렬
# 구간 i~j 사이 숫자를 모두 뒤집음 x 2
# 초기 상태로 되돌리려면 어떠한 구간을 뒤집어야하는지

## 주어진 것
# 1. 숫자 판의 크기
# 2. 두번 뒤집힌 상태의 숫자 배치

## 출력해야하는 것
# 뒤집어야 할 구간을 차례로 출력

## 알 수 있는 것
# 숫자가 제 자리에 있지 않다면 뒤집혀야하는 구간
# 뒤집혀있는 가장 끝 숫자부터 뒤집어보면 됨

# 한 구간이 뒤집혀져있고 그 안에 있는 부분이 뒤집혀있다면 나중에 뒤집힌 부분은 정렬되어있을거임

# 만약 한 구간이 뒤집혀져있고 그 끝을 중간으로 뒤집혀있다면?,,,

# 입력 : 숫자판을 나타내는 정수 이후 두번 뒤집힌 숫자 배열


class TwoFlipNumber:
    def __init__(self, number_length, numbers):
        self.number_length = number_length
        self.numbers = numbers
        self._numbers = self.numbers.copy()

    def is_sorted_numbers(self):
        for i in range(self.number_length):
            if self._numbers[i] != i + 1:
                return False
        return True

    def find_flip_number(self):
        for i in range(self.number_length):
            if self._numbers[i] != i+1:
                return i, self._numbers.index(i+1)
        return 0, 0

    def reverse_find_flip_number(self):
        for i in range(self.number_length-1, -1, -1):
            if self._numbers[i] != i+1:
                return self._numbers.index(i+1), i
        return 0, 0

    def flip_numbers(self, index1, index2):
        self._numbers[index1:index2+1] = self._numbers[index1:index2+1][::-1]

    def solution(self):
        flipped_number, index_number = self.find_flip_number()
        self.flip_numbers(flipped_number, index_number)
        index_number2, flipped_number2 = self.reverse_find_flip_number()
        self.flip_numbers(index_number2, flipped_number2)

        if self.is_sorted_numbers():
            print(flipped_number+1, index_number+1)
            print(index_number2+1, flipped_number2+1)
            return

        self._numbers = self.numbers

        index_number, flipped_number = self.reverse_find_flip_number()
        self.flip_numbers(index_number, flipped_number)
        flipped_number2, index_number2 = self.find_flip_number()
        self.flip_numbers(flipped_number2, index_number2)

        print(index_number+1, flipped_number+1)
        print(flipped_number2+1, index_number2+1)




if __name__ == "__main__":
    n = int(input().strip())
    v = list(map(int, input().strip().split()))

    # n = 10
    # v = [1, 2, 3, 4, 8, 7, 6, 5, 9, 10] ## 한번 뒤집은 거
    # v = [1, 2, 8, 4, 3, 7, 6, 5, 9, 10]

    # 5-8, 3-8

    two_flip_num = TwoFlipNumber(n, v)
    two_flip_num.solution()