n, *l = open(0).read().split()
i = 1
while 1:
    if len({e[-i:]for e in l}) == int(n):
        print(i)
        break
    i+=1