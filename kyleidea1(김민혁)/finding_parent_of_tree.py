import sys
input = sys.stdin.readline

from collections import deque
n = int(input())

l = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    l[a].append(b)
    l[b].append(a)

parent = [0] * (n+1)

q = deque([1])

while q:
    v = q.popleft()
    for child in l[v]:
        if parent[child] == 0:
            parent[child] = v
            q.append(child)

for i in range(2,len(parent)):
    print(parent[i])

