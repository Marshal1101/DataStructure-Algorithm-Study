import sys


def get_damage_battle(Hatk, Eatk, Ehp):
    turn = (Ehp // Hatk) + (1 if Ehp % Hatk else 0)
    return (turn - 1) * Eatk

def main():
    input= sys.stdin.readline
    N, Hatk = map(int, input().split())
    HPmax = HPcur = 0
    for i in range(N):
        t, a, h = map(int, input().split())
        if t == 1:
            ret = get_damage_battle(Hatk, a, h)
            # print("i:", i, "dam:", ret)
            HPcur += ret
            if HPcur > HPmax:
                HPmax = HPcur 
        else:
            Hatk += a
            HPcur -= h
            if HPcur < 0: HPcur = 0
            # print("i:", i, "hatk:", Hatk, "HPcur:", HPcur)
    
    print(HPmax + 1)


if __name__ == '__main__':
    main()