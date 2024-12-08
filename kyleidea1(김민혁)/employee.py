import sys

T = int(input())
for _ in range(T):
    n = int(input())
    q = []
    cnt = 1
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        q.append((a,b))
    q.sort()
    tmp = q[0][1]
    for i in range(n):
        if q[i][1] < tmp:
            cnt += 1
            tmp = q[i][1]
    print(cnt)