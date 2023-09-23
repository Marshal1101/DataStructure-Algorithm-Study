import sys


class Monomino:
    def __init__(self, color, width=4, deep=4, light=2) -> None:
        self.color = color
        self.width = width
        self.deep = deep
        self.light = light
        self.len = deep+light
        self.lines = [[0] * width for _ in range(self.len)]
        self.btm_idx = 0
        self.full = [False] * self.len
        self.height = [0] * self.width
        self.boom_cnt = 0
        
    # 내부함수: 인덱스 rc의 다음 블록이 들어갈 높이위치를 찾아서 해당 높이로 쌓기
    def __add(self, rc):
        btm = self.btm_idx 
        h = self.height[rc]
        self.lines[(btm+h)%self.len][rc] = 1
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

    # 라인 초기화
    def __clear(self, idx:int):
        for i in range(self.width):
            self.lines[idx][i] = 0
        self.full[idx] = False

    # 라인 찼는지 체크
    def __check_full(self) -> bool:
        is_full = False
        btm = self.btm_idx
        for h in range(self.deep):
            for v in self.lines[(btm+h)%self.len]:
                if v == 0:
                    break
            else:
                self.full[(btm+h)%self.len] = True
                is_full = True
        return is_full
    
    # 터진 후 블록 다시 하강
    def __re_add(self, ci:list, idx:int):
        mh = 0
        for i in ci:
            if mh < self.height[i]:
                mh = self.height[i]
        for i in ci:
            self.height[i] = mh
        for i in ci:
            self.__add(i)
            self.lines[idx][i] = 0


    def height_btm_to_idx(self, idx:int) -> int:
        btm = self.btm_idx
        if btm > idx:
            h = idx + self.len - btm
        else:
            h = idx - btm
        return h

    # 블록 삽입 후 과정
    def check(self):
        boom_cnt = 0
        btm = self.btm_idx
        while self.__check_full():

            # if self.color == 0:
            #     print("b")
            #     self.show()

            # 터진 라인 인덱스 저장
            boom_idx = []
            for h in range(self.deep):
                idx = (btm+h)%self.len
                if self.full[idx]:
                    boom_cnt += 1
                    boom_idx.append(idx)
                    self.__clear(idx)

            # 가장 낮게 터진 라인 밑으로 다음 블록 들어갈 위치로 높이 갱신
            bi = boom_idx[0]
            for i in range(self.width):
                h_idx = bi
                k = 0
                while k < self.deep:
                    idx = (bi + self.len - k) % self.len
                    if self.lines[idx][i] != 0:
                        break
                    h_idx = idx
                    if idx == btm:
                        break
                    k += 1
                self.height[i] = self.height_btm_to_idx(h_idx)
            
            # if self.color == 0:
            #     print("c")
            #     self.show()


            # 가장 낮게 터진 라인 위로 블록들 다시 하강
            idx = bi
            end = (btm+self.len-1) % self.len
            h = 1
            while h < self.len:
                idx = (bi + h) % self.len
                ci = []
                for i in range(self.width):
                    if self.lines[idx][i]:
                        ci.append(i)
                    elif ci:
                        self.__re_add(ci, idx)
                        ci = []
                if ci:
                    self.__re_add(ci, idx)
                if idx == end:
                    break
                h += 1

            # if self.color == 0:
            #     print("a")
            #     self.show()

            # if self.color == 0:
            #     self.show()

        # 점수 기록
        self.boom_cnt += boom_cnt

        # 옅은 구역 체크
        over_cnt = self.__check_over()
        if over_cnt > 0:
            for h in range(over_cnt):
                self.__clear((btm+h)%self.len)
            self.btm_idx = (self.btm_idx + over_cnt) % self.len
        for i in range(self.width):
            if self.height[i] >= over_cnt:
                self.height[i] -= over_cnt
            else:
                self.height[i] = 0


    # 블록이 옅은 색 라인에 있는지 체크, 블록 있는 라인개수 반환
    def __check_over(self) -> int:
        over_cnt = 0
        btm = self.btm_idx
        for i in range(self.deep, self.len):
            for v in self.lines[(btm+i)%self.len]:
                if v == 1:
                    over_cnt += 1
                    break
        return over_cnt
    

    # 남은 칸 개수 반환
    def count(self) -> int:
        cnt = 0
        idx = 0
        while idx < self.len:
            for v in self.lines[idx]:
                if v == 1:
                    cnt += 1
            idx += 1
        
        return cnt
    
    # 점수 반환
    def point(self) -> int:
        return self.boom_cnt
    

    # 도미노 상태 프린트해보기
    def show(self):
        btm = self.btm_idx
        for i in range(self.len):
            idx = (btm+i)%self.len
            print(self.lines[idx], idx)
        print(self.height, "height[i]", "btm:", btm)


def main():
    input = sys.stdin.readline
    N = int(input())
    green = Monomino(0)
    blue = Monomino(1)
    for k in range(N):
        t, x, y = map(int, input().split())
        green.insert(t, x, y)
        green.check()
        blue.insert(t, x, y)
        blue.check()
        # print("green", k, "input:", t, x, y)
        # green.show()
        print("blue", k, "input:", t, x, y)
        blue.show()

    # print("green:", green.point(), green.count())
    # print("blue:", blue.point(), blue.count())

    print(green.point() + blue.point())
    print(green.count() + blue.count())


if __name__ == '__main__':
    main()