import sys


def permutation(src:str, num:int, cl:int, visited:set, tmp:list):
    global cnt, ans
    if cnt > num:
        return
    if cl == len(src):
        cnt += 1
        if cnt == num:
            ans = "".join(tmp)
        return
    for i in range(len(src)):
        if not src[i] in visited:
            visited.add(src[i])
            tmp.append(src[i])
            permutation(src, num, cl+1, visited, tmp)
            tmp.pop()
            visited.remove(src[i])


def main():
    input = sys.stdin.readline
    while (line := input().rstrip()) != "":
        src, num = line.split()
        num = int(num)
        end = 1
        for k in range(len(src), 1, -1):
            end *= k
        if num > end:
            print(line + " = No permutation")
            continue
        visited = set()
        tmp = []
        global cnt, ans
        cnt = 0
        permutation(src, num, 0, visited, tmp)
        print(line + " = " + ans)



if __name__ == '__main__':
    main()



while (line := input().strip()) != "":
    st, n = map(str, line.split())
    n = int(n)
    # 방문여부
    visited = [False] * len(st)
    cnt = 0
    result = permutation(st, 0, "", n)
    if result == None:
        print("{0} {1} = No permutation".format(st, n))
    else:
        print("{0} {1} = {2}".format(st, n, result))