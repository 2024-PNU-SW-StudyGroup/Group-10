import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int,input().split()))

dp = [1]*n

for i in range(1,n):
    for j in range(i):
        if l[j] < l[i]:
            dp[i] = max(dp[i],dp[j]+1)

lis = []

max_dp = max(dp)
max_idx = dp.index(max_dp)
while max_idx >= 0:
    if dp[max_idx] == max_dp:
        lis.append(l[max_idx])
        max_dp -= 1
    max_idx -= 1

lis.reverse()

print(len(lis))
print(*lis)