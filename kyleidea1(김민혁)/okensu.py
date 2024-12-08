import sys
input = sys.stdin.readline

n = int(input())
stack = []
l = list(map(int,input().strip().split()))
dp = [-1]*n

for i in range(n):
    while stack and l[stack[-1]] < l[i]:
        v = stack.pop()
        dp[v] = l[i]
    stack.append(i)

print(' '.join(map(str,dp)))