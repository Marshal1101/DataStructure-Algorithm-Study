import sys


def bf_check(cnt: int, used_op: str):
    # 종료
    if cnt == N-1:
        total = 0
        num = N
        tmp = ""
        i = len(used_op)-1
        is_sq = False
        while num > 1:
            if used_op[i] == "+":
                if is_sq:
                    total += int(tmp)
                    tmp = ""
                    is_sq = False
                else:
                    total += num

            elif used_op[i] == "-":
                if is_sq:
                    total -= int(tmp)
                    tmp = ""
                    is_sq = False
                else:
                    total -= num

            elif used_op[i] == " ":
                if len(tmp) > 0: tmp = str(num-1) + tmp
                else: tmp = str(num-1) + str(num)
                is_sq = True

            i -= 1
            num -= 1

        if is_sq: total += int(tmp)
        else: total += 1

        global result
        if total == 0:
            ans = "1" 
            for i in range(2, N+1):
                ans += used_op[i-2]
                ans += str(i)
            result += ans + "\n"
        return

    bf_check(cnt+1, used_op+" ")
    bf_check(cnt+1, used_op+"+")
    bf_check(cnt+1, used_op+"-")


input = sys.stdin.readline
T = int(input())
global result
result = ""

for _ in range(T):
    N = int(input())
    bf_check(0, "")
    result += "\n"

print(result)