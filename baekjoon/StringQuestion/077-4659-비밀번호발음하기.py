import sys; input = sys.stdin.readline


def check_pwd(pwd: str) -> bool:
    hasVowel = False
    vowel = set(["a", "e", "i", "o", "u"])
    prev = pwd[0]
    is_prev_vowel = False
    equal_cnt = 0
    if prev in vowel:
        hasVowel = True
        is_prev_vowel = True
        equal_cnt = 1
    else:
        is_prev_vowel = False
        equal_cnt = -1

    for i in range(1, len(pwd)):
        c = pwd[i]
        if c in vowel:
            hasVowel = True
            if is_prev_vowel: equal_cnt += 1
            else: equal_cnt = 1
            is_prev_vowel = True
        else:
            if is_prev_vowel: equal_cnt = -1
            else: equal_cnt -= 1
            is_prev_vowel = False

        if prev == c and c != "e" and c != "o":
            return False

        if equal_cnt == 3 or equal_cnt == -3:
            return False
        
        prev = c

    if (hasVowel): return True
    else: return False


while (line := input().rstrip()) != "end":
    if check_pwd(line):
        print(f"<{line}> is acceptable.")
    else:
        print(f"<{line}> is not acceptable.")
