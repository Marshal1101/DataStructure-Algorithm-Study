def self_num(n: int):
    total = n
    for s in str(n) :
        total += int(s)
    return total


def main():
    check_list = [False] * 10036
    i = 1
    while i <= 10000:
        check_list[self_num(i)] = True
        i += 1
    for i in range(1, 10000):
        if not check_list[i]:
            print(i)

if __name__ == '__main__':
    main()