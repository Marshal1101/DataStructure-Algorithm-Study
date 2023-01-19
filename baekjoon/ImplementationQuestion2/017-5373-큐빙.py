"""
루빅스 큐브 3x3x3
각면에 있는 9개 색이 동일해야한다.

큐브가 풀린 상태, 색정렬된 상태에서 시작
위: 흰색, 아래: 노란색, 앞: 빨강, 뒷: 주황, 왼:초록, 오:파란

큐브를 돌린 방법이 순서대로 주어질 때, 가장 위면의 색상을 구하시요

첫째 줄에 큐브를 돌린 횟수 n이 주어진다. (1 ≤ n ≤ 1000)
둘째 줄에는 큐브를 돌린 방법이 주어진다.
각 방법은 공백으로 구분되어져 있으며, 첫 번째 문자는 돌린 면이다.
U: 윗 면, D: 아랫 면, F: 앞 면, B: 뒷 면, L: 왼쪽 면, R: 오른쪽 면이다.
두 번째 문자는 돌린 방향이다.
+인 경우에는 시계 방향 (그 면을 바라봤을 때가 기준), -인 경우에는 반시계 방향이다.

"""

import sys


class Node:
    # 요소는 6색 정보를 가진다.
    # 회전 시에는 한 축을 중심으로 제자리 회전한다.
    def __init__(self, key, up="w", down="y", front="r", back="o", left="g", right="b") -> None:
        self.key = key
        self.up = up
        self.down = down
        self.front = front
        self.back = back
        self.left = left
        self.right = right


class Cube:
    # 큐브
    """
    U====================
            010203
            040506
            070809
    L==========F==========R
    010407  070809  090603
    222510  101112  122624
    191613  131415  151821
    D=====================
            131415
            161718
            192021
    B=====================
            192021
            222324
            010203
    U=====================
    """
    def __init__(self, key=None) -> None:
        self.key = None
        self.nodes = [Node(i) for i in range(27)]
        self.plane_dict = {}
        self.plane_dict["U"] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.plane_dict["F"] = [7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.plane_dict["D"] = [13, 14, 15, 16, 17, 18, 19, 20, 21]
        self.plane_dict["B"] = [19, 20, 21, 22, 23, 24, 1, 2, 3]
        self.plane_dict["L"] = [1, 4, 7, 22, 25, 10, 19, 16, 13]
        self.plane_dict["R"] = [9, 6, 3, 12, 26, 24, 15, 18, 21]


    def plane_rotate(self, com):
        """
        plane idx position
        012
        345
        678
        """
        side, wise = com
        plane = self.plane_dict[side]
        if wise == "+":
            for up, right, down, left in ((0, 2, 8, 6), (1, 5, 7, 3)):
                tmp = self.nodes[plane[up]]
                self.nodes[plane[up]] = self.nodes[plane[left]]
                self.nodes[plane[left]] = self.nodes[plane[down]]
                self.nodes[plane[down]] = self.nodes[plane[right]]
                self.nodes[plane[right]] = tmp
        elif wise == "-":
            for up, right, down, left in ((0, 2, 8, 6), (1, 5, 7, 3)):
                tmp = self.nodes[plane[up]]
                self.nodes[plane[up]] = self.nodes[plane[right]]
                self.nodes[plane[right]] = self.nodes[plane[down]]
                self.nodes[plane[down]] = self.nodes[plane[left]]
                self.nodes[plane[left]] = tmp

        for key in self.plane_dict[side]:
            self.node_rotate(self.nodes[key], side, wise)


    def node_rotate(self, node:Node, side, wise):
        # x축: front: +X, back: -X
        if side == "F" or side == "B":
            d = 1   # 앞면 볼 때 시계방향
            if side == "B": d *= -1
            if wise == "-": d *= -1
            if d == 1:
                tmp = node.up
                node.up = node.left
                node.left = node.down
                node.down = node.right
                node.right = tmp
            elif d == -1:
                tmp = node.up
                node.up = node.right
                node.right = node.down
                node.down = node.left
                node.left = tmp

        # y축: left: +Y, right: -Y
        if side == "L" or side == "R":
            d = 1   # 왼쪽면 볼 때 시계방향
            if side == "R": d *= -1
            if wise == "-": d *= -1
            if d == 1:
                tmp = node.up
                node.up = node.back
                node.back = node.down
                node.down = node.front
                node.front = tmp
            elif d == -1:
                tmp = node.up
                node.up = node.front
                node.front = node.down
                node.down = node.back
                node.back = tmp
        
        # z축: up: +Z, down: -Z
        if side == "U" or side == "D":
            d = 1   # 위쪽 볼 때 시계방향
            if side == "D": d *= -1
            if wise == "-": d *= -1
            if d == 1:
                tmp = node.back
                node.back = node.left
                node.left = node.front
                node.front = node.right
                node.right = tmp
            elif d == -1:
                tmp = node.back
                node.back = node.right
                node.right = node.front
                node.front = node.left
                node.left = tmp

    def output(self, side):
        ans = ""
        if side == "U":
            for k in range(0, 9, 3):
                for i in range(k, k+3):
                    key = self.plane_dict[side][i]
                    ans += self.nodes[key].up
                if k != 6: ans += '\n'
        # elif side == "D":
        #     for k in range(0, 9, 3):
        #         for i in range(k, k+3):
        #             key = self.plane_dict[side][i]
        #             ans += self.nodes[key].down
        #         ans += '\n'
        # elif side == "F":
        #     for k in range(0, 9, 3):
        #         for i in range(k, k+3):
        #             key = self.plane_dict[side][i]
        #             ans += self.nodes[key].front
        #         ans += '\n'
        # elif side == "B":
        #     for k in range(0, 9, 3):
        #         for i in range(k, k+3):
        #             key = self.plane_dict[side][i]
        #             ans += self.nodes[key].back
        #         ans += '\n'
        # elif side == "L":
        #     for k in range(0, 9, 3):
        #         for i in range(k, k+3):
        #             key = self.plane_dict[side][i]
        #             ans += self.nodes[key].left
        #         ans += '\n'
        # elif side == "R":
        #     for k in range(0, 9, 3):
        #         for i in range(k, k+3):
        #             key = self.plane_dict[side][i]
        #             ans += self.nodes[key].right
        #         ans += '\n'
        print(ans)


def main():
    input = sys.stdin.readline
    T = int(input())
    for i in range(T):
        N = int(input())
        cube = Cube()
        commands = input().split()
        for com in commands:
            # print("=============", com, end=" ")
            cube.plane_rotate(com)
        cube.output("U")



if __name__ == '__main__':
    main()