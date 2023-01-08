import sys


def translater(string: str)->str:
    # print(f"{string} => ", end="")
    if 64 < ord(string[0]) < 91:
        return "Error!"
    if ord(string[0]) == 95 or ord(string[-1]) == 95:
        return "Error!"

    is_java = []
    is_cpp = False
    ans = ""
    prev = 0
    for i in range(len(string)):
        asc = ord(string[i])
        if 64 < asc < 91:
            is_java.append(i)
        elif asc == 95:
            if prev == 95:
                is_java.append(0)
                break
            is_cpp = True
        prev = asc
    
    if is_java and is_cpp:
        return "Error!"

    elif is_java:
        ans += string[:is_java[0]]
        for i in range(1, len(is_java)):
            ans += "_" + string[is_java[i-1]].lower()
            ans += string[is_java[i-1]+1:is_java[i]]
        ans += "_" + string[is_java[-1]].lower()
        ans += string[is_java[-1]+1:]       
        return ans

    elif is_cpp:
        arr = string.split('_')
        ans += arr[0]
        for i in range(1, len(arr)):
            ans += arr[i][0].upper() + arr[i][1:]
        return ans

    else: return string


def main():
    input = sys.stdin.readline
    while (string := input().rstrip()) != "":
        print(translater(string))


if __name__=='__main__':
    main()