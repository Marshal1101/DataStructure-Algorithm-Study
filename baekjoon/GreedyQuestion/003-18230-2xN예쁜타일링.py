import sys


def main():
    input = sys.stdin.readline
    N, A, B = map(int, input().split())
    t1 = list(map(int, input().split()))
    t2 = list(map(int, input().split()))
    
    t1.sort()
    t2.sort()

    ans = 0
    i = 0
    last_t1 = 0
    last_t2 = 0
    while i < N:
        if t1 and t2:
            if i + 2 <= N:
                if len(t1) > 1:
                    if t1[-1] + t1[-2] <= t2[-1]:
                        last_t2 = t2.pop()
                        ans += last_t2
                        i += 2
                    else:
                        last_t1 = t1.pop()
                        ans += last_t1
                        i += 1
                        
                elif t1[-1] <= t2[-1]/2:
                    last_t2 = t2.pop()
                    ans += last_t2
                    i += 2
                else:
                    last_t1 = t1.pop()
                    ans += last_t1
                    i += 1
            else:
                last_t1 = t1.pop()
                ans += last_t1
                i += 1
                
        elif t2 and i + 2 <= N:
            last_t2 = t2.pop()
            ans += last_t2
            i += 2
        elif t1:
            last_t1 = t1.pop()
            ans += last_t1
            i += 1
        else:
            if t2 and i + 1 == N:
                ans -= last_t1
                t1.append(last_t1)
                last_t2 = t2.pop()
                ans += last_t2
                i += 1


        # print(f"{i} of {N}, ==> {ans}")

    print(ans)

if __name__ == '__main__':
    main()