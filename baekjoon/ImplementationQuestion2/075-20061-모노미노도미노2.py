import sys


"""
둘째 줄부터 N개의 줄에 블록을 놓은 정보가 한 줄에 하나씩 순서대로 주어지며, t x y와 같은 형태이다.
t = 1: 크기가 1×1인 블록을 (x, y)에 놓은 경우
t = 2: 크기가 1×2인 블록을 (x, y), (x, y+1)에 놓은 경우
t = 3: 크기가 2×1인 블록을 (x, y), (x+1, y)에 놓은 경우
"""

class Line(object):
    def __init__(self, length=4) -> None:
        self.length = length                    # 라인 너비
        self.arr = [0 for _ in range(length)]   # 라인 초기 값 [0, 0, 0, 0]
        self.is_full = False                    # 라인이 찼는지 [1, 1, 1, 1]일 떄, True


class Monomino(object):
    def __init__(self, color=0, width=4, deep=4, light=2) -> None:
        self.color = color          # 컬러 그린:0 블루:1
        self.width = width          # 폭 
        self.deep = deep            # 짙은구간 깊이
        self.light = light          # 옅은구간 깊이
        self.len = deep + light     # 전체 깊이
        # 라인 번호와 라인들의 바닥부터 시작하는 초기 순서: [0,1,2,3,4,5]
        self.line_num = [i for i in range(self.len)]
        # 바닥 라인번호를 가리키는 초기 포인터: 0
        self.btm_head = 0
        # 라인객체 생성, 인덱스가 라인객체의 번호가 된다.
        self.lines = [Line(width) for _ in range(self.len)]
        # 다음 블록이 쌓일 높이 너비 인덱스 0, 1, 2, 3의 각각
        self.height = [0] * (width)
        # 점수
        self.boom_cnt = 0


    # 내부함수: 인덱스 rc의 다음 블록이 들어갈 높이위치를 찾아서 해당 높이로 쌓기
    def __add(self, rc):
        # self.btm_head: 밑바닥 라인번호을 가리키는 시작포인터
        # self.height[rc]: rc에 블록이 내려오면 위치할 높이, 밑바닥부터에서 0 ~ 5
        # self.line_num[self.btm_head]: 바닥 라인의 번호
        # line_num = self.line_num[(self.btm_head + cur_h)%self.len] 이것은
        # 밑바닥라인에서부터 높이 cur_h인 라인의 번호
        cur_h = self.height[rc]
        line_num = self.line_num[(self.btm_head + cur_h)%self.len]
        self.lines[line_num].arr[rc] = 1
        self.height[rc] += 1

    # 블록삽입
    def insert(self, t, r, c):
        rc = r if self.color else c
        
        # 입력되는 블록모양이 녹색과 파란색은 서로 반대 형태다. 파란판은 2->3, 3->2 반대로 전환
        if self.color:
            if t == 2: t = 3
            elif t == 3: t = 2

        # 한 칸 입력
        if t == 1:
            self.__add(rc)

        # 가로블록, 나란히 두칸 입력
        elif t == 2:
            # 더 높은 칸 기준으로 높이 맞추고 삽입
            if self.height[rc] < self.height[rc+1]:
                self.height[rc] = self.height[rc+1]
            else:
                self.height[rc+1] = self.height[rc]
            
            self.__add(rc)
            self.__add(rc+1)

        # 세로블록, 위아래 두칸 연달아 입력
        elif t == 3:
            self.__add(rc)
            self.__add(rc)


    # 내부함수: Line 리스트 값 초기화 [0, 0, 0, 0]
    def __clear(self, line:object) -> None:
        for i in range(line.length):
            line.arr[i] = 0
        line.is_full = False


    # 내부함수: 삭제될 라인 체크해서 터질 라인은 .is_full = True
    def __check_full(self) -> bool:
        btm = self.btm_head
        i = 0
        is_full = False
        while i < self.deep:
            line_num = self.line_num[(btm+i)%self.len]
            
            for v in self.lines[line_num].arr:
                if v == 0:
                    break
            else:
                self.lines[line_num].is_full = True
                is_full = True
            i += 1

        return is_full
    
    # 내부함수: 라인 하나가 제거되면 블록이 들어갈 각 인덱스의 높이도 전부 1씩 내림
    def __down(self):
        btm = self.btm_head
        for i in range(self.width):
            while self.height[i] > 0:
                self.height[i] -= 1
                line_num = self.line_num[(btm+self.height[i])%self.len]
                if self.lines[line_num].arr[i] != 0:
                    self.height[i] += 1
                    break


    # 삭제할 라인 점검하고 갱신
    def delete(self) -> None:
        boom_cnt = 0
        # 가득 찬 라인을 삭제하고 라인 순서 재배치

        while self.__check_full():
            btm = self.btm_head
            i = 0
            boom_line = []  # 폭발된 라인 번호
            keep_line = []  # 유지된 라인 번호
            while i < self.len:
                idx = (btm+i)%self.len
                line_num = self.line_num[idx]
                # 해당 라인이 터질 라인이면
                if self.lines[line_num].is_full:
                    boom_line.append(line_num)             # 폭발된 라인그룹에 추가
                    self.__clear(self.lines[line_num])     # 해당 라인 초기화 [0, 0, 0, 0], False
                    boom_cnt += 1                       # 폭발 횟수 + 1
                else:
                    keep_line.append(line_num)             # 유지된 라인그룹에 추가
                i += 1
            # 새로운 라인순서 [유지] + [폭발(초기화됨)]
            self.line_num = keep_line + boom_line
            # 라인순서 전체를 갱신했으므로 밑바닥 가리키는 포인터는 0
            self.btm_head = 0
        
        self.__down()                       # 전체 블록 높이 -1

        # 점수 기록
        self.boom_cnt += boom_cnt

        # 옅은 구역으로 블록 초과되었는지 체크
        # 초과된 개수만큼 (over_cnt = 0~2) self.btm_head가 가리키는 밑바닥라인부터 초기화
        over_cnt = self.__check_over()
        if over_cnt > 0:
            btm = self.btm_head
            for i in range(over_cnt):
                line_num = self.line_num[(btm+i)%self.len]     # 밑바닥 라인인덱스을 찾아서
                self.__clear(self.lines[line_num])             # 라인을 초기화
            # 바닥포인터를 삭제한 수만큼 다음 라인번호로 이동하여 가리킴
            self.btm_head = (btm + over_cnt) % self.len
            self.__down()                               # 블록위치 높이 -1

    # 내부함수: 블록이 옅은 색 라인에 있는지 체크, 블록 있는 라인개수 반환
    def __check_over(self) -> int:
        over_cnt = 0
        btm = self.btm_head
        for i in range(self.deep, self.len):
            line_num = self.line_num[(btm+i)%self.len]
            for v in self.lines[line_num].arr:
                if v == 1:
                    over_cnt += 1
                    break
        return over_cnt


    # 남은 칸 개수 반환
    def count(self) -> int:
        cnt = 0
        btm = self.btm_head
        i = 0
        while i < self.deep:
            cur_idx = self.line_num[(btm+i)%self.len]
            for v in self.lines[cur_idx].arr:
                if v == 1:
                    cnt += 1
            i += 1
        
        return cnt
    
    # 점수 반환
    def point(self) -> int:
        return self.boom_cnt
    

    # 도미노 상티 프린트해보기
    def show(self):
        print("라인인덱스 순서:", self.line_num, "바닥포인터:", self.btm_head)
        btm = self.btm_head
        i = 0
        while i < self.len:
            cur_idx = self.line_num[(btm+i)%self.len]
            print(self.lines[cur_idx].arr, cur_idx)
            i += 1
        print(self.height, "height[i]")


def main():
    input = sys.stdin.readline
    N = int(input())
    green = Monomino(0)
    blue = Monomino(1)
    for k in range(N):
        t, x, y = map(int, input().split())
        green.insert(t, x, y)
        green.delete()
        blue.insert(t, x, y)
        blue.delete()
        # print("green", k)
        # green.show()
        # print("blue", k)
        # blue.show()

    print(green.point() + blue.point())
    print(green.count() + blue.count())


if __name__ == '__main__':
    main()