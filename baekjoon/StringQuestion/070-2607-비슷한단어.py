import sys

def compare(ref: str, word: str) -> bool:
    if abs(len(ref) - len(word)) > 1: return False

    ref_cnt = [0] * 26
    for c in ref:
        ref_cnt[ord(c)-65] += 1

    isPossible = True
    if len(ref) == len(word):
        copy_ref_cnt = ref_cnt[:]
        for c in word:
            copy_ref_cnt[ord(c)-65] -= 1

        isInsChar = False
        isDelChar = False
        for n in copy_ref_cnt:
            if abs(n) > 1:
                isPossible = False
                break
            if n == -1:
                if not isDelChar: isDelChar = True
                else: 
                    isPossible = False 
                    break
            if n == 1:
                if not isInsChar: isInsChar = True
                else:
                    isPossible = False
                    break

    elif len(ref) - len(word) == 1:
        copy_ref_cnt = ref_cnt[:]
        for c in word:
            copy_ref_cnt[ord(c)-65] -= 1

        isInsChar = False
        for n in copy_ref_cnt:
            if abs(n) > 1:
                isPossible = False
                break
            if n == -1:
                isPossible = False 
                break
            if n == 1:
                if not isInsChar: isInsChar = True
                else:
                    isPossible = False
                    break
            
    else: 
        copy_ref_cnt = ref_cnt[:]
        for c in word:
            copy_ref_cnt[ord(c)-65] -= 1

        isDelChar = False
        for n in copy_ref_cnt:
            if abs(n) > 1:
                isPossible = False
                break
            if n == 1:
                isPossible = False 
                break
            if n == -1:
                if not isDelChar: isDelChar = True
                else:
                    isPossible = False
                    break
        
    if isPossible: return True
    else: return False

def main():
    input = sys.stdin.readline
    N = int(input())
    ref = input().rstrip()
    ans = 0
    for _ in range(N-1):
        if compare(ref, input().rstrip()):
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()