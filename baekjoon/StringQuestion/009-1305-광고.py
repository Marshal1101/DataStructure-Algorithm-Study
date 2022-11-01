import sys


def get_partial_match(search: str) -> list:
    M = len(search)
    pi = [0] * M
    begin = 1
    matched = 0
    while begin + matched < M:
        if search[begin + matched] == search[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        
        else:
            if matched == 0:
                begin += 1
            
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]

    return pi


def main():
    input = sys.stdin.readline
    L = int(input())
    string = input().rstrip()
    pi = get_partial_match(string)
    print(L - pi[len(pi)-1])


if __name__ == '__main__':
    main()