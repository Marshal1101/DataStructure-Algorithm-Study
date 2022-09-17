import sys
from collections import defaultdict


def find(follow, x) :
    # print(x, 'finding', follow[x])
    if follow[x] != x :
        follow[x] = find(follow, follow[x])
    return follow[x]


def union(friend, follow, a, b) :
    a = find(follow, a)
    b = find(follow, b)
    if len(friend[a]) < len(friend[b]) :
        # print(a, 'following', b)
        follow[a] = b
        friend[b].update(friend[a])
        return b
    else :
        # print(b, 'following', a)
        follow[b] = a
        friend[a].update(friend[b])
        return a


def main() :
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T) :
        F = int(input())
        friend = defaultdict(set)
        follow = defaultdict(int)
        for _ in range(F) :
            f1, f2 = input().split()
            if not follow[f1] :
                follow[f1] = f1
                friend[f1].add(f1)
                # print(f1, 'first followed', follow[f1])
            if not follow[f2] : 
                follow[f2] = f2
                friend[f2].add(f2)
                # print(f2, 'first followed', follow[f2])
            if (tf := find(follow, f1)) != find(follow, f2) :
                f = union(friend, follow, f1, f2)
                # print('followee', f)
                print(len(friend[f]))
            else : 
                # print('f1=f2:', 'f1:', f1)
                print(len(friend[tf]))


if __name__ == '__main__' :
    main()