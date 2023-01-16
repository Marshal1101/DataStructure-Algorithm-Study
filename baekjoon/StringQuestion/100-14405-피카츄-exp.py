s=input()                       # s = "pikaqiu"
for i in['pi','ka','chu']:s=s.replace(i,'*')
print(s)                        # **qiu
print(*s)                       # * * q i u
print({*s})                     # {'q', '*', 'i', 'u'}
print([{*s}!={'*'}])            # [True]
print("YNEOS"[{*s}!={'*'}::2])  # NO