import sys
s = sys.stdin.readline().strip()
num = []
ops = []
tmp = ""
for i in s:
    if i.isdigit():
        tmp += i
    else:
        num.append(tmp)
        tmp = ""
        ops += i
num.append(tmp)

ans = []
for i in range(len(num)):
    for j in range(i+2, len(num)+1):
        print(i,j)