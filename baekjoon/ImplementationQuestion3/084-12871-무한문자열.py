def main():
    s = input().rstrip()
    t = input().rstrip()

    if len(s) < len(t):
        s, t = t, s
    ll = len(s)
    ls = len(t)
    i = j = 0
    while i < ll:
        while j < ls:
            if i >= ll:
                i = 0
            if s[i] != t[j]:
                print(0)
                return
            i += 1
            j += 1
        if i < ll:
            j = 0
    print(1)

if __name__ == '__main__':
    main()


## 빠른 답
a=input()
b=input()
print(1 if a*len(b)==b*len(a) else 0)