# https://www.acmicpc.net/source/53597033

N = int(input())
R = int(input())
reco = list(map(int, input().split()))

picture = {}

for i in reco:
    if picture.get(i):
        picture[i] = picture[i] + 1
    else:
        if len(picture) >= N:
            del(picture[sorted(picture.items(), key=lambda x: x[1])[0][0]])
        picture[i] = 1

print(*sorted(picture.keys()))