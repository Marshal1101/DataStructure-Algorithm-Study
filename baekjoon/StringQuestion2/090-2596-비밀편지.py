def main():
    N = int(input())
    msg = input().rstrip()
    num = ["000000", "001111", "010011", "011100", "100110", "101001", "110101", "111010"]

    ans = ""
    for i in range(N):
        pos = [0] * 8
        for j in range(6):
            c = msg[6*i + j]
            for k in range(8):
                if c != num[k][j]:
                    pos[k] += 1
        
        min_dif = 6
        min_k = -1
        fail = False
        for k in range(8):
            if pos[k] < min_dif:
                fail = False
                min_dif = pos[k]
                min_k = k
            elif pos[k] == min_dif:
                fail = True

        if not fail:
            ans += chr(min_k+65)
        else: 
            print(i+1)
            return

    print(ans)


if __name__ == '__main__':
    main()
