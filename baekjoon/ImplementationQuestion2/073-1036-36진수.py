import sys

def conv36to10(num:str)->int:
    nl = len(num)
    deci = 0
    for i in range(nl):
        cn = ord(num[nl-1-i])
        if cn > 64:
            deci += (cn-55) * 36 ** i
        else:
            deci += (cn-48) * 36 ** i
    return deci


def conv10to36(num:int)->str:
    if num == 0: return 0
    ret = []
    while num != 0:
        div = num % 36
        if div < 10:
            ret.append(str(div))
        else:
            ret.append(chr(div+55))
        num = num // 36
    return "".join(reversed(ret))


def main():
    input = sys.stdin.readline
    N = int(input())
    arr = [input().rstrip() for _ in range(N)]
    K = int(input())

    arr.sort(key=lambda x: (-len(x), x))
    arr = list(map(list, arr))
    ans = 0

    # 초기 10진수
    for num in arr:
        deci = 0
        nl = len(num)
        for i in range(nl):
            deci += conv36to10(num[nl-1-i]) * 36 ** i
        ans += deci

    # 최대증가분 합산
    if K > 0:
        diff = [0] * 36
        for num in arr:
            nl = len(num)
            for i in range(nl):
                cn = ord(num[nl-1-i])
                if cn > 64:
                    dn = (cn-55)
                else:
                    dn = (cn-48)
                diff[dn] += (35-dn) * 36 ** i
        diff.sort(reverse=True)
        for i in range(K):
            ans += diff[i]

    print(conv10to36(ans))


if __name__ == '__main__':
    main()