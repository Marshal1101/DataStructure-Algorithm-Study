import sys


def brute_force(src: str, search: str) -> list:
    ret = []
    begin = 0
    while (begin + len(search) <= len(src)):
        matched = True
        for i in range(len(search)):
            if src[begin + i] != search[i]:
                matched = False
                break

        if matched:
            ret.append(begin)
            
        begin += 1
    
    return ret


def get_partial_match(search: str) -> list:
    M = len(search)
    pi = [0] * M
    begin = 1
    matched = 0

    while begin + matched < M:
        if search[begin + matched] == search[matched]:
            matched += 1
            pi[begin+matched-1] = matched

        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched-1]

    return pi


def KMP_search(src: str, search: str) -> list:
    ret = []
    N = len(src)
    M = len(search)

    pi = get_partial_match(search)

    begin = 0
    matched = 0
    while begin <= N - M:
        if matched < M and src[begin + matched] == search[matched]:
            matched += 1
            if matched == M:
                ret.append(begin)

        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched-1]

    return ret


def main():
    input = sys.stdin.readline
    T = int(input())
    ret = []
    for _ in range(T):
        N = int(input())
        numbers = []
        for _ in range(N):
            curr_num = input().rstrip()
            flag = False
            for prev_num in numbers:
                pi = brute_force(curr_num, prev_num)
                # print("pi", pi)
                if pi and pi[0] == 0:
                    ret.append("NO")
                    flag = True
                    break
            numbers.append(curr_num)
            if flag: break
        else: ret.append("YES")
        
    print("\n".join(ret))


if __name__ == '__main__':
    main()