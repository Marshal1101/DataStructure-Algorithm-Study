## 문자열 - 신규 아이디 추천 (미구현)


# - 77
# _ 95
# . 78

# ~ 126
# ! 33
# @ 64
# # 35
# $ 36
# % 69
# ^ 94
# & 38
# * 42
# ( 40
# ) 41
# = 61
# + 43
# [ 91
# { 123
# ] 93
# } 125
# : 58
# ? 63
# , 44
# < 60
# > 62
# / 47

# UPPER A 65 ~ 90 Z
# lower a 97 ~ 122 z

def solution(new_id):
    n = len(new_id)
    capitals = list(new_id)
    answer = []
    spotflag = False
    null_cnt = 0
    LIMIT = 14
    
    p1 = []
    for i in range(n) :
        ASCII = ord(capitals[i])

        # 마침표 78 ( . ) 체크: 첫 .은 남기고, 다음엔 삭제
        if ASCII == 46 :
            null_cnt += 1
            if spotflag == True :
                continue
            else :
                spotflag = True
                p1.append(ASCII)
        else :
            spotflag = False

        # 빼기 45
        if ASCII == 45 :
            p1.append(ASCII)
            continue

        # 밑줄 95
        if ASCII == 95 :
            p1.append(ASCII)
            continue

        # 숫자
        if 48 <= ASCII <= 57 :
            p1.append(ASCII)

        # 65 ~ 90 (대문자) 소문자 변환 +32
        elif 65 <= ASCII <= 90 :
            ASCII += 32
            p1.append(ASCII)

        # 소문자
        elif 97 <= ASCII <= 122 :
            p1.append(ASCII)

    # 첫 글자 '.' 이면 삭제
    if p1[0] == 46 :
        del p1[0]

    # 마지막 '.' 이면 삭제
    while p1 :
        if p1[-1] == 46 :
            del p1[-1]
        else :
            break


    # 1차 후 길이 체크
    k = len(p1)

    # 문자열 없으면 a 대입, is_empty 플래그
    is_empty = False
    if k == 0 :
        is_empty = True
        p1.append('a')
        k += 1

    # 2자 이하라면 길이 3이 될 때까지 마지막 문자 추가
    while k < 3 :
        p1.append(p1[-1])
        k += 1

    # 15자 슬라이스 그리고 마지막에 마침표 제거
    p2 = p1[:15]
    while p2 :
        if p2[-1] == 46 :
            del p2[-1]
        else :
            break

    # p2 길이체크
    j = len(p2)

    # 아스키코드를 문자로 변환된 answer 생성
    if is_empty :
        return ''.join(p2)
    else :
        answer = ''
        for i in range(j) :
            answer += chr(p2[i])

        return answer

print(solution("=.="))