try:
    while (i:=input()):
        N, M = map(int, i.split())
        print(N, M, "=>", end= " ")

        if N >= 3 and M >= 7:
            print(5 + M-7)

        else:
            if N >= 3:
                if M >= 4:
                    print(4)
                else:
                    print(M)
            elif N == 2:
                if M <= 7:
                    print((M+1)//2)
                else:
                    print(4)
            else:
                print(1)
except:
    exit(0)


"""
체스 나이트 움직임 오른쪽만 이동

위치 가장 왼쪽아래 칸에서 시작
2칸 위, 1칸 오
1칸 위, 2칸 오
1칸 아, 2칸 오
2칸 아, 1칸 오

이동회수가 4이상이면,
이동방법 모두 한 번씩 사용해야한다.
이동회수가 4미만이면,
(방문한 칸이 5개미만, =시작위치포함하는듯)
이동방법에 대한 제약 없다.

방문할 수 있는 칸의 최대개수 구해라


입력: 세로 가로 N M
N, M은 2,000,000,000 이하인 자연수


아이디어
일단 오른쪽으로만 이동한다.
한 번 오른쪽 가면 왼쪽으로 이동 불가
현재 j 열보다 낮은 열 다신 못 간다.
최대한 오른쪽으로 가지 않으면서 이동해야함

체스판이 크다. 완전탐색 안 되게 생김.

방문회수 5이상이면(이동4이상면)
이동방법 한 번씩은 써야함

1 1
1
ans 1

2 2
10
00
ans 1

2 4
1000
0020
ans 2

2 5
10003
00200
ans 3

2 6
100030
002000
ans 3

2 7
1000300
0020004

2 8
10003000
00200040




3 2
10
00
02

2 3
100
002
ans 2

3 3
103
002
020
ans 3

3 4
1030
0023
0204
ans 4

3 5
10303
00234
02043
ans 4

3 6
103030
002030
020400
ans 4

3 7
1030005
0000400
0200000
ans 5


4 2
10
00
02
00

4 3
103
000
020
000

4 4
1030
0023
0204
0003
ans 4

4 5
10303
00234
02000
00030
ans 4

4 8
10300000
00000500
02000000
00004000
00300000


4 7
1030005
0003400
0200040
0000000


5 5
10000
00204
02000
00030
00000
ans 4

4 6
103030
002340
020004
000300
ans 4

4 7
1000005
0020400
0200000
0003000
ans 5

열 길이에 최대 개수가 달렸다.
행이 최소 4이상
열이 최소 7이상
되어야 중복제한 해제 가능
개수 5이후로 이동방법 중복가능?

4 13
100000507090B
0020400006000
02000006080A0
0003000000000
ans 11

50-7=43

5 + 43 = 48

또는
행이 최소 3이면
1030005000
0000400000
0200000000


17 5
10000
00001
01000
00010
00000
.....


오른쪽으로 최소 한 칸은 간다.
오1 and 위2 또는 아래2
오2 and  위1 또는 아래1

"""