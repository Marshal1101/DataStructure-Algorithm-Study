def chk_straight(card):
    for i in range(1, len(card)):
        if card[i][0] - card[i-1][0] != 1:
            return 0
    return card[-1][0]

def chk_flush(card):
    color = card[0][1]
    for i in range(1, len(card)):
        if color != card[i][1]:
            return 0
    return card[-1][0]

def chk_count(card):
    count = dict()
    for num, color in card:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    count = list(count.items())
    count.sort(key=lambda x: (x[1], x[0]), reverse=True)
    ret = 0
    if count[1][1] == 2:
        if count[0][1] == 3:
            ret += count[0][0] * 10
            ret += count[1][0]
            ret += 700
        elif count[0][1] == 2:
            ret += count[0][0] * 10
            ret += count[1][0]
            ret += 300
    elif count[0][1] == 4:
        ret += count[0][0]
        ret += 800
    elif count[0][1] == 3:
        ret += count[0][0]
        ret += 400
    elif count[0][1] == 2:
        ret += count[0][0]
        ret += 200
    else:
        ret += count[0][0]
        ret += 100
    return ret


def main():
    card = []
    for _ in range(5):
        color, num = input().split()
        card.append((int(num), color))

    card.sort()
    is_straight = chk_straight(card)
    is_flush = chk_flush(card)

    ans = chk_count(card)
    if is_straight and is_flush:
        print(900 + is_straight)
    elif ans > 700:
        print(ans)
    elif is_flush:
        print(600 + is_flush)
    elif is_straight:
        print(500 + is_straight)
    else:
        print(ans)


if __name__ == '__main__':
    main()