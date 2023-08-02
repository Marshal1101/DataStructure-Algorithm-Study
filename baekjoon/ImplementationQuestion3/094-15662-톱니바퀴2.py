import sys


def get_rotate_list(main_gn, main_dr, graph) -> list:
    ret = []
    l_gn = main_gn - 1
    r_gn = main_gn + 1
    l_dr = r_dr = main_dr

    while l_gn >= 0:
        if graph[l_gn][2] == graph[l_gn+1][6]:
            break
        l_dr = -l_dr
        ret.append((l_gn, l_dr))
        l_gn -= 1

    while r_gn < len(graph):
        if graph[r_gn][6] == graph[r_gn-1][2]:
            break
        r_dr = -r_dr
        ret.append((r_gn, r_dr))
        r_gn += 1
    
    return ret

def simulate(graph, command) -> None:
    for main_gn, main_dr in command:
        main_gn -= 1
        sub_command = get_rotate_list(main_gn, main_dr, graph)
        # print(f"=====com: {main_gn}, {main_gn}, {sub_command}")
        rotate(main_gn, main_dr, graph)
        for gn, dr in sub_command:
            rotate(gn, dr, graph)
    print(score(graph))


def rotate(gn: int, dr: int, graph: list) -> None:
    # print(f"rotate, gear num: {gn}, direction.rot: {dr}")
    gear = graph[gn]
    if dr == 1:
        tmp = gear[7]
        for i in range(7, 0, -1):
            gear[i] = gear[i-1]
        gear[0] = tmp
    elif dr == -1:
        tmp = gear[0]
        for i in range(7):
            gear[i] = gear[i+1]
        gear[7] = tmp

def score(graph) -> int:
    ret = 0
    for i in range(len(graph)):
        if graph[i][0]: ret += 1
    return ret


def main():
    input = sys.stdin.readline
    N = int(input())
    graph = [list(map(int, input().rstrip())) for _ in range(N)]
    K = int(input())
    command = [list(map(int, input().split())) for _ in range(K)]
    simulate(graph, command)


if __name__=='__main__':
    main()
