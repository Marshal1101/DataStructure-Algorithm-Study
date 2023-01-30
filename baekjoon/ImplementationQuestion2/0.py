from collections import Counter

sbo = "0001111122334455555"
sbo_list = list(map(int, sbo))

c = Counter(sbo)
print(c)
print(c.most_common())

cl = Counter(sbo_list)
print(cl)
cl.pop(0)
print(cl)
cl_sort = cl.most_common()
cl_sort.sort(key=lambda x: (x[1], x[0]))
print(cl_sort)
