X = int(input())
stk = [(1<<6)]
while (tmp:=sum(stk)) != X:
    stk[-1] >>= 1
    if sum(stk) < X:
        stk.append(stk[-1])

print(len(stk))

# print(X.bit_count())