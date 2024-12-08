import sys
n = int(input())
l = []
for _ in range(n):
    s,e = map(int, sys.stdin.readline().strip().split())
    l.append((s,e))

l = sorted(l, key = lambda x: x[0])
l = sorted(l, key = lambda x: x[1])

start = l[0][0]
end = l[0][1]
cnt = 1

for s,e in l[1:]:
    if s >= end:
        start,end = s,e
        cnt += 1

print(l)