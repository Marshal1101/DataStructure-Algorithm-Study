import sys

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        a, b = map(int, input().split())
        while a:
            x = (b-1)//a + 1    ## 주석1
            a = a * x - b
            b = b * x
        print(x)


if __name__ == '__main__':
    main()


"""주석1

https://www.acmicpc.net/board/view/24576

@uytr083 기약분수를 입력 받았을 때 분모를 동일하게 하기 위해서 입니다.

예를 들면
1
1 12
라는 입력이 들어왔을떄 (b - 1) / a + 1 을 하게 되면 12가 나오나
b / a + 1 을 할 경우에는 13 이 나오게 되어서 답이 156 이 나오게 됩니다.
다른 경우에는 상관이 없습니다. 진분수 이므로 분모는 무조건 분자보다 크기 때문에
a + 1 = b 인 경우에도 첫번째 분모가 2가 나오기 때문에 상관 없습니다.

"""