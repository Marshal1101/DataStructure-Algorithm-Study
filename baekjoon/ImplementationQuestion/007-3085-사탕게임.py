import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    graph = [list(input().rstrip()) for _ in range(N)]
    total_max = 0
    for i in range(N):
        max_seq = [0, 0, 0]
        cur_seq = [0, 0, 0]
        prev_color = graph[i][0]
        is_connect = False
        for j in range(N):
            if graph[i][j] == prev_color:
                cur_seq[0] += 1
            else:
                cur_seq[2] = j
                front_connect = rear_connect = cur_seq[0]
                if not is_connect:
                    if cur_seq[1] > 0:
                        if (i > 0 and graph[i-1][cur_seq[1]-1] == prev_color) \
                            or (i < N-1 and graph[i+1][cur_seq[1]-1] == prev_color):
                            front_connect += 1
                        elif cur_seq[1]-1 > 0 and graph[i][cur_seq[1]-2] == prev_color:
                            front_connect += 1
                    
                    if j < N:
                        if (i > 0 and graph[i-1][j] == prev_color) \
                            or (i < N-1 and graph[i+1][j] == prev_color):
                            if j < N-1 and graph[i][j+1] == prev_color:
                                cur_seq[0] += 1
                                is_connect = True
                                continue
                            rear_connect += 1
                        elif j < N-1 and graph[i][j+1] == prev_color:
                            rear_connect += 1
                    
                    cur_seq[0] = max(front_connect, rear_connect)
                
                if cur_seq[0] > max_seq[0]:
                    max_seq = cur_seq[:]
                cur_seq = [1, j, j]
                prev_color = graph[i][j]
                is_connect = False
            
        if not is_connect:
            if cur_seq[1] > 0:
                if (i > 0 and graph[i-1][cur_seq[1]-1] == prev_color) \
                    or (i < N-1 and graph[i+1][cur_seq[1]-1] == prev_color):
                    cur_seq[0] += 1
                elif cur_seq[1]-1 > 0 and graph[i][cur_seq[1]-2] == prev_color:
                    cur_seq[0] += 1

        if cur_seq[0] > total_max:
            total_max = cur_seq[0]

        if max_seq[0] > total_max:
            total_max = max_seq[0]

    for j in range(N):
        max_seq = [0, 0, 0]
        cur_seq = [0, 0, 0]
        prev_color = graph[0][j]
        is_connect = False
        for i in range(N):
            if graph[i][j] == prev_color:
                cur_seq[0] += 1
            else:
                cur_seq[2] = i
                front_connect = rear_connect = cur_seq[0]
                if not is_connect:
                    if cur_seq[1] > 0:
                        if (j > 0 and graph[cur_seq[1]-1][j-1] == prev_color) \
                            or (j < N-1 and graph[cur_seq[1]-1][j+1] == prev_color):
                            front_connect += 1
                        elif cur_seq[1]-1 > 0 and graph[cur_seq[1]-2][j] == prev_color:
                            front_connect += 1
                    
                    if i < N:
                        if (j > 0 and graph[i][j-1] == prev_color) \
                            or (j < N-1 and graph[i][j+1] == prev_color):
                            if i < N-1 and graph[i+1][j] == prev_color:
                                cur_seq[0] += 1
                                is_connect = True
                                continue
                            rear_connect += 1
                        elif i < N-1 and graph[i+1][j] == prev_color:
                            rear_connect += 1
                    
                    cur_seq[0] = max(front_connect, rear_connect)

                if cur_seq[0] > max_seq[0]:
                    max_seq = cur_seq[:]
                cur_seq = [1, i, i]
                prev_color = graph[i][j]
                is_connect = False

        if not is_connect:
            if cur_seq[1] > 0:
                if (j > 0 and graph[cur_seq[1]-1][j-1] == prev_color) \
                    or (j < N-1 and graph[cur_seq[1]-1][j+1] == prev_color):
                    cur_seq[0] += 1
                elif cur_seq[1]-1 > 0 and graph[cur_seq[1]-2][j] == prev_color:
                    cur_seq[0] += 1
        
        if cur_seq[0] > total_max:
            total_max = cur_seq[0]

        if max_seq[0] > total_max:
            total_max = max_seq[0]
                
    print(total_max)


if __name__=='__main__':
    main()