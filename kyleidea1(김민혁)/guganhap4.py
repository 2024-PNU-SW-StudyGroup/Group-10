n,m = map(int,input().split())
l = list(map(int,input().split()))

ps = [0]*(len(l)+1)
for i in range(1,len(ps)):
    ps[i] = ps[i-1] + l[i-1]

for i in range(m):
    s,e = map(int,input().split())
    print(ps[e]-ps[s-1])