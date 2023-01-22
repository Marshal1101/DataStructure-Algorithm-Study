import sys


def main():
    input = sys.stdin.readline
    e = {}
    e[0] = [None, None, None]
    ptr = 0
    for i, v in enumerate(input().rstrip()):
        new = [v, ptr, None]
        e[i+1] = new
        e[ptr][2] = i + 1
        ptr = i + 1
    serial = ptr + 1

    M = int(input())
    for _ in range(M):
        com = input().split()
        if com[0] == "L":
            if e[ptr][1] != None:
                ptr = e[ptr][1]
                
        elif com[0] == "D":
            if e[ptr][2] != None:
                ptr = e[ptr][2]

        elif com[0] == "B":
            if ptr != 0:
                e[e[ptr][1]][2] = e[ptr][2]
                if e[ptr][2] != None:
                    e[e[ptr][2]][1] = e[ptr][1]
                ptr = e[ptr][1]

        elif com[0] == "P":
            if e[ptr][2] != None:
                new = [com[1], ptr, e[ptr][2]]
                e[serial] = new
                e[ptr][2] = serial
                e[e[serial][2]][1] = serial
            else:
                new = [com[1], ptr, None]
                e[serial] = new
                e[ptr][2] = serial            

            ptr = serial
            serial += 1


    head = 0
    ans = ""
    while e[head][2] != None:
        head = e[head][2]
        ans += e[head][0]

    print(ans)
    

if __name__ == '__main__':
    main()