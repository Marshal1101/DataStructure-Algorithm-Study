import sys


def cross_word(src: str, target: str) -> str:
    char_arr = [-1] * 26
    src_macth_idx = len(src)
    target_match_idx = len(target)

    for j in range(len(src)):
        if char_arr[ord(src[j])-65] < 0:
            char_arr[ord(src[j])-65] = j

    for i in range(len(target)):
        if char_arr[ord(target[i])-65] != -1:
            if char_arr[ord(target[i])-65] < src_macth_idx:
                src_macth_idx = char_arr[ord(target[i])-65]
                target_match_idx = i
            

    # print(f"src_macth_idx: {src_macth_idx}\ntarget_match_idx: {target_match_idx}")
    ret = ""
    for i in range(len(target)):
        if i == target_match_idx:
            ret += src
        else:
            for j in range(len(src)):
                if j == src_macth_idx:
                    ret += target[i]
                else: ret += "."
        ret += "\n"
    
    return ret


src, target = sys.stdin.readline().split()
print(cross_word(src, target))