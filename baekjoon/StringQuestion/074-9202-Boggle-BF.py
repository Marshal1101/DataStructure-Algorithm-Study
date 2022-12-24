import sys


def add_point(word):
    if len(word) < 3: return 0
    elif len(word) < 5: return 1
    elif len(word) == 5: return 2
    elif len(word) == 6: return 3
    elif len(word) == 7: return 5
    elif len(word) == 8: return 11


def dfs(curr_word, si, sj, board, words, visited, first_idx, first_char_arr):
    if len(curr_word) == 8: return

    global point
    global longstr  
    global matched

    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]

    for k in range(8):
        ni = si + di[k]
        nj = sj + dj[k]
        if 0 <= ni < 4 and 0 <= nj < 4 and not visited[ni][nj]:
            visited[ni][nj] = True
            curr_word += board[ni][nj]
            if curr_word in words and not curr_word in matched:
                matched.add(curr_word)
                point += add_point(curr_word)
                first_char_arr[first_idx] -= 1
                if len(curr_word) > len(longstr):
                    longstr = curr_word
                elif len(curr_word) == len(longstr) and curr_word < longstr:
                    longstr = curr_word
            dfs(curr_word, ni, nj, board, words, visited, first_idx, first_char_arr)
            curr_word = curr_word[:-1]
            visited[ni][nj] = False



def boggle(board, words, first_char_arr):
    global point
    point = 0
    global longstr
    longstr = ""
    global matched
    matched = set()
    
    for i in range(4):
        for j in range(4):
            first_char = board[i][j]
            if (first_char_arr[(first_idx := ord(first_char)-65)]) > 0:
                visited = [[False] * 4 for _ in range(4)]
                visited[i][j] = True
                dfs(first_char, i, j, board, words, visited, first_idx, first_char_arr)
    
    print(point, longstr, len(matched))


def main():
    input = sys.stdin.readline
    W = int(input())
    words = set()
    first_char_arr = [0] * 26
    for _ in range(W):
        words.add(word := input().rstrip())
        first_char_arr[ord(word[0])-65] += 1
    input()

    B = int(input())
    for b in range(B):
        board = [list(input().rstrip()) for _ in range(4)]
        boggle(board, words, first_char_arr[:])
        
        if b < B-1: input()


if __name__ == '__main__':
    main()