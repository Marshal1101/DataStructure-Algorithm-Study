import sys


def palindrome(string: str) -> int:
    lp = 0
    rp = len(string) - 1
    moveLp = True
    moveRp = True
    while lp < rp:
        if string[lp] != string[rp]:
            if string[lp+1] == string[rp]:
                tlp = lp + 1
                trp = rp
                while tlp < trp:
                    if string[tlp] != string[trp]:
                        moveLp = False
                        break
                    tlp += 1
                    trp -= 1
                if moveLp: return 1

            if string[lp] == string[rp-1]:
                trp = rp - 1
                tlp = lp
                while tlp < trp:
                    if string[tlp] != string[trp]:
                        moveRp = False
                        break
                    tlp += 1
                    trp -= 1
                if moveRp: return 1

            return 2
        
        lp += 1
        rp -= 1
    
    return 0


def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        string = input().rstrip()
        print(palindrome(string))


if __name__ == '__main__':
    main()