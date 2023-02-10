# https://www.acmicpc.net/source/55020355

import sys
from copy import deepcopy

def input(dtype=int):
    return dtype(sys.stdin.readline().strip())

def input_list(dtype=int):
    return [dtype(i) for i in sys.stdin.readline().strip().split()]

C = [
    [
        ['w', 'w', 'w'],
        ['w', 'w', 'w'],
        ['w', 'w', 'w'],
    ],
    [
        ['y', 'y', 'y'],
        ['y', 'y', 'y'],
        ['y', 'y', 'y'],
    ],
    [
        ['r', 'r', 'r'],
        ['r', 'r', 'r'],
        ['r', 'r', 'r'],
    ],
    [
        ['o', 'o', 'o'],
        ['o', 'o', 'o'],
        ['o', 'o', 'o'],
    ],
    [
        ['g', 'g', 'g'],
        ['g', 'g', 'g'],
        ['g', 'g', 'g'],
    ],
    [
        ['b', 'b', 'b'],
        ['b', 'b', 'b'],
        ['b', 'b', 'b'],
    ],
]
F = {'U': 0, 'D': 1, 'F': 2, 'B': 3, 'L': 4, 'R': 5}
S = {
    'U': [
        ('F', (0,0), (0,1), (0,2)), 
        ('L', (0,0), (0,1), (0,2)), 
        ('B', (2,2), (2,1), (2,0)), 
        ('R', (0,0), (0,1), (0,2)),
    ], 
    'D': [
        ('F', (2,0), (2,1), (2,2)), 
        ('R', (2,0), (2,1), (2,2)), 
        ('B', (0,2), (0,1), (0,0)), 
        ('L', (2,0), (2,1), (2,2)),
    ], 
    'F': [
        ('U', (2,0), (2,1), (2,2)), 
        ('R', (0,0), (1,0), (2,0)), 
        ('D', (0,2), (0,1), (0,0)), 
        ('L', (2,2), (1,2), (0,2)),
    ], 
    'B': [
        ('U', (0,0), (0,1), (0,2)), 
        ('L', (2,0), (1,0), (0,0)), 
        ('D', (2,2), (2,1), (2,0)), 
        ('R', (0,2), (1,2), (2,2)),
    ], 
    'L': [
        ('U', (0,0), (1,0), (2,0)), 
        ('F', (0,0), (1,0), (2,0)), 
        ('D', (0,0), (1,0), (2,0)), 
        ('B', (0,0), (1,0), (2,0)),
    ], 
    'R': [
        ('U', (0,2), (1,2), (2,2)), 
        ('B', (0,2), (1,2), (2,2)), 
        ('D', (0,2), (1,2), (2,2)), 
        ('F', (0,2), (1,2), (2,2)),
    ], 
}

def spin(C, f, d):
    if d == '+':
        C[F[f]] = list(map(list, zip(*reversed(C[F[f]]))))
        (F1, *ij1), (F2, *ij2), (F3, *ij3), (F4, *ij4) = S[f]
        for (i1, j1), (i2, j2), (i3, j3), (i4, j4) in zip(ij1, ij2, ij3, ij4):
            C[F[F1]][i1][j1], C[F[F2]][i2][j2], C[F[F3]][i3][j3], C[F[F4]][i4][j4] = \
                C[F[F4]][i4][j4], C[F[F1]][i1][j1], C[F[F2]][i2][j2], C[F[F3]][i3][j3]
    else:
        C[F[f]] = list(reversed(list(map(list, zip(*C[F[f]])))))
        (F1, *ij1), (F2, *ij2), (F3, *ij3), (F4, *ij4) = S[f]
        for (i1, j1), (i2, j2), (i3, j3), (i4, j4) in zip(ij1, ij2, ij3, ij4):
            C[F[F1]][i1][j1], C[F[F2]][i2][j2], C[F[F3]][i3][j3], C[F[F4]][i4][j4] = \
                C[F[F2]][i2][j2], C[F[F3]][i3][j3], C[F[F4]][i4][j4], C[F[F1]][i1][j1]

for _ in range(input()):
    N = input()
    A = input_list(str)
    C_ = deepcopy(C)
    for a in A:
        spin(C_, a[0], a[1])

    print("\n".join(map(lambda r: "".join(r), C_[0])))