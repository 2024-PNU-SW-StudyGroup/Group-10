import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().strip().split()))

dp = [1]*(n)

for i in range(1,n):
    for j in range(i):
        if l[i] > l[j]:
            if l[i] > l[j] and dp[i] < dp[j]+1:
                dp[i] = dp[j] + 1

max_dp = max(dp)
max_idx = dp.index(max_dp)
lis = []

while max_idx >= 0:
    if dp[max_idx] == max_dp:
        lis.append(l[max_idx])
        max_dp -= 1
    max_idx -= 1
lis.reverse()

print(dp)
print(len(lis))
print(*lis)