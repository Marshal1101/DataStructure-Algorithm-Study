arr = []
for a, b in zip(map(int, input().rstrip()), map(int, input().rstrip())):
    arr.append(a)
    arr.append(b)

while len(arr) > 2:
    new = []
    num = arr.pop()
    while arr:
        new.append((num + arr[-1]) % 10)
        num = arr.pop()
    arr = new

print("".join(map(str, arr)))