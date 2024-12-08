import sys
input = sys.stdin.readline

n = int(input())
tri = [[] for _ in range(n)]

for i in range(n):
    l = list(map(int,input().split()))
    tri[i] = l

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            tri[i][j] += tri[i-1][0]
        elif j == i:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] = max(tri[i-1][j-1], tri[i-1][j]) + tri[i][j]

print(max([max(l) for l in tri]))