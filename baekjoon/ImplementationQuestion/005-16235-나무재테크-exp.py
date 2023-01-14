# https://www.acmicpc.net/source/53889861

def grow_tree(ground, tree, k):
    new_tree = dict()
    dead_tree = dict()
    for (y,x,age),cnt in sorted(tree.items(), key=lambda x:x[0][2]):
        g = ground[y-1][x-1] + add_ground[y-1][x-1]*k
        if g >= age:
            if g // age >= cnt:
                ground[y-1][x-1] -= age*cnt
                age += 1
                if (y,x,age) in new_tree:
                    new_tree[(y,x,age)] += cnt
                else:
                    new_tree[(y,x,age)] = cnt
            else:
                ground[y-1][x-1] -= (g // age) * age
                if (y,x,age) in dead_tree:
                    dead_tree[(y,x,age)] += cnt - g // age
                else:
                    dead_tree[(y,x,age)] = cnt - g // age
                cnt = g // age
                age += 1
                if (y,x,age) in new_tree:
                    new_tree[(y,x,age)] += cnt
                else:
                    new_tree[(y,x,age)] = cnt
            if age % 5 == 0:
                for dy, dx in direct:
                    ny, nx = y+dy, x+dx
                    if 0 <= ny-1 < n and 0 <= nx-1 < n:
                        if (ny,nx,1) in new_tree:
                            new_tree[(ny,nx,1)] += cnt
                        else:
                            new_tree[(ny,nx,1)] = cnt
        else:
            if (y,x,age) in dead_tree:
                dead_tree[(y,x,age)] += cnt
            else:
                dead_tree[(y,x,age)] = cnt
    for (y,x,age),cnt in dead_tree.items():
        ground[y-1][x-1] += (age//2) * cnt
    return new_tree, ground

import sys
input = sys.stdin.readline
direct = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
n, m, k = map(int, input().split())
ground = [[5 for _ in range(n)] for _ in range(n)]
add_ground = [list(map(int,input().split())) for _ in range(n)]
tree = {tuple(map(int,input().split())):1 for _ in range(m)}
for i in range(k):
    tree, ground = grow_tree(ground, tree, i)
print(sum(tree.values()))