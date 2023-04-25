import sys

input = lambda dtype=int: dtype(sys.stdin.readline().strip())
input_list = lambda dtype=int: [dtype(i) for i in sys.stdin.readline().strip().split()]

N, M = input_list()
B = [[-1] * (N+2)] + [[-1] + input_list() + [-1] for _ in range(N)] + [[-1] * (N+2)]

def Find_block():
    V = [[B[i][j] < 0 for j in range(N+2)] for i in range(N+2)]
    max_block = (0, 0, 0, 0, [])

    for si in range(1, N+1):
        for sj in range(1, N+1):
            if V[si][sj] or B[si][sj] == 0: continue 

            bnum = B[si][sj]
            rnum = 0
            V[si][sj] = True
            Q = [(si, sj)]
            R = []
            idx = 0
            while idx < len(Q):
                i, j = Q[idx]
                idx += 1
                for _i, _j in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if not V[_i][_j]:
                        if B[_i][_j] == 0:
                            V[_i][_j] = True 
                            R.append((_i, _j))
                            Q.append((_i, _j))
                            rnum += 1
                        elif B[_i][_j] == bnum:
                            V[_i][_j] = True
                            Q.append((_i, _j))
            
            max_block = max(max_block, (len(Q), rnum, si, sj, Q))
            for i, j in R:
                V[i][j] = False

    return max_block[-1]

def Gravity():
    for j in range(1, N+1):
        floor = N + 1
        for i in range(N, 0, -1):
            if B[i][j] >= 0 and i+1 < floor:
                B[floor-1][j] = B[i][j]
                B[i][j] = -2
                floor -= 1
            elif B[i][j] > -2:
                floor = i

def Rotate(B):
    return list(reversed(list(map(list, zip(*B)))))

S = 0
MB = Find_block()
while len(MB) > 1:
    S += len(MB) ** 2
    for i, j in MB:
        B[i][j] = -2

    Gravity()
    B = Rotate(B)
    Gravity()
    MB = Find_block()

print(S)