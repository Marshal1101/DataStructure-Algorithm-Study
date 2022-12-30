import sys


line = sys.stdin.readline().strip()
happy_cnt = 0
sad_cnt = 0
for i in range(len(line)):
    if i > 1 and line[i] == ")":
        if line[i-2] == ":" and line[i-1] == "-":
            happy_cnt += 1
    
    elif i > 1 and line[i] == "(":
        if line[i-2] == ":" and line[i-1] =="-":
            sad_cnt += 1

if happy_cnt == 0 and sad_cnt == 0:
    print("none")
elif happy_cnt == sad_cnt:
    print("unsure")
elif happy_cnt > sad_cnt:
    print("happy")
else:
    print("sad")
