import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
l = []

for _ in range(n):
    x = int(input())
    l.append(x)

print(round(sum(l)/n))
l.sort()
print(l[(n//2)])
c = sorted(Counter(l).items(), key = lambda x:x[1], reverse = True)
print((c[1][0] if c[0][1] == c[1][1] else c[0][0]) if len(c) > 1 else c[0][0])
print(max(l)-min(l))