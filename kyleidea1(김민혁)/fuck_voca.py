import sys
input = sys.stdin.readline

a,b = map(int,input().split())
dic = dict()
for _ in range(a):
    inp = input().strip()
    if len(inp) >= b:
        if inp in dic:
            dic[inp] += 1
        else:
            dic[inp] = 1
dic = dict(sorted(dic.items(), key = lambda x:x[0]))
dic = dict(sorted(dic.items(), key = lambda x:len(x[0]), reverse = True))
dic = sorted(dic.items(), key = lambda x:x[1], reverse = True)

for word in dic:
    print(word[0])