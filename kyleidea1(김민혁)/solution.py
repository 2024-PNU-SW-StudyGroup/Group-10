n = int(input())
l = list(map(int,input().split()))
l.sort(key = lambda x:abs(x))
idx = 0
s = l[0]+l[1]
minn = abs(s)

for i in range(1,n-1):
    tmp = s
    s += l[i+1]-l[i-1]
    if abs(s)<minn:
        minn = abs(s)
        idx = i
print(min(l[idx],l[idx+1]),max(l[idx],l[idx+1]))