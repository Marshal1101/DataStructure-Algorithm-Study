num = input().rstrip()

log = set()
prev = ""
while prev != num:
    if not num in log: log.add(num)
    else: 
        print("NFA")
        break
    prev = num
    num = str(int(num[0]) * len(num))


print("FA")