# 12015 Gold 2
# BS Solution_O(nlogn)
# Find the length of LIS

import sys
import bisect
input = sys.stdin.readline

n = int(input())
l = list(map(int,input().split()))

dp = [l[0]]

for i in range(n):
    if l[i] > dp[-1]:
        dp.append(l[i])
    else:
        dp[bisect.bisect_left(dp,l[i])] = l[i]

print(dp)
print(len(dp))