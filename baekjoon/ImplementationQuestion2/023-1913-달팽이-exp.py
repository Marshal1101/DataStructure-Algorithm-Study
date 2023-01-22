delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def fill():
    table = [[0] * N for _ in range(N)]
    pos = ()
    i = j = d = 0
    di, dj = delta[0]
    for n in range(N*N, 0, -1):
        if n == M:
            pos = (i+1, j+1)
        table[i][j] = f'{n}'
        if i+di >= N or i+di < 0 or j+dj >= N or j+dj < 0 or table[i+di][j+dj]:
            d = (d+1)%4
            di, dj = delta[d]
        i, j = i+di, j+dj
    for t in table:
        print(' '.join(t))
    print(*pos)

N = int(input())
M = int(input())
fill()