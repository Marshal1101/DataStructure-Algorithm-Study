import sys


def main():
    A = sys.stdin.readline().rstrip()
    T = sys.stdin.readline().rstrip()

    A = list(A)
    len_A = len(A)
    rev_A = A[::-1]
    pre = []
    suf = []

    si = 0
    ei = len(T)-1

    # 앞
    is_pre = True
    while si <= ei:

        if is_pre:
            pre.append(T[si])
            si += 1
            if pre[-len_A:] == A:
                pre[-len_A:] = []
                is_pre = False

        else:
            suf.append(T[ei])
            ei -= 1
            if suf[-len_A:] == rev_A:
                suf[-len_A:] = []
                is_pre = True

    while suf:
        pre.append(suf.pop())
        if pre[-len_A:] == A:
            pre[-len_A:] = []

    ans = "".join(pre)
    print(ans)

if __name__ == '__main__':
    main()