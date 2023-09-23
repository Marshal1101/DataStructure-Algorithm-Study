def main():
    N = int(input())
    if N == 1:
        print("*")
        return
    
    R = 4 * N - 1
    C = 4 * N - 3

    board = [[" "] * C for _ in range(R)]
    star = N
    si = 0
    sj = 0
    ei = 1
    ej = C-1
    while star > 1:
        width = star * 4 - 3
        height = star * 4 - 1
        for j in range(sj, sj+width):
            board[si][j] = "*"
            board[si+height-1][j] = "*"
        for i in range(si, si+height):
            board[i][sj] = "*"
            board[i][sj+width-1] = "*"
        
        board[ei][ej] = " "
        board[ei+1][ej-1] = "*"
        si += 2
        sj += 2
        ei += 2
        ej -= 2
        star -= 1
    board[si][sj] = "*"
    board[si+1][sj] = "*"
    board[si+2][sj] = "*"

    for j in range(1, C):
        board[1][j] = ""

    for b in board:
        print("".join(b))


if __name__ == '__main__':
    main()