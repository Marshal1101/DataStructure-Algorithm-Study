board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# def rotate(board):
#     # p1 = [list(reversed(b[:])) for b in board]
#     p1 = [b[:] for b in board]
#     for b in p1:
#         print(b)
#     p2 = list(map(list, zip(*p1)))
#     print()
#     for b in p2:
#         print(b)
#     print()
#     for p in p2:
#         p.reverse()
#     for b in p2:
#         print(b)
#     print()

# rotate(board)

def rotate_board(board):

    ret = list(map(list, zip(*[line[:] for line in board])))
    print(ret)
    for r in ret:
        r.reverse()
    return ret

for b in rotate_board(board):
    print(b)