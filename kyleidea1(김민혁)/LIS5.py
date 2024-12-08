# 14003 Platinum 5
# BS Solution_O(nlogn)
# Find one specific LIS

import sys
import bisect
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

dp = [l[0]]
valid_ends_indices = [0]  # LIS를 만족하는 각 값의 인덱스

parent = [-1] * n # 각 원소의 이전 원소 인덱스를 저장. 역추적용

for i in range(1, n):
    if l[i] > dp[-1]:
        parent[i] = valid_ends_indices[-1]
        dp.append(l[i])
        valid_ends_indices.append(i)
    else:
        idx = bisect.bisect_left(dp, l[i])
        dp[idx] = l[i]
        valid_ends_indices[idx] = i
        if idx > 0:
            parent[i] = valid_ends_indices[idx - 1]

# LIS 재구성
lis = []
index = valid_ends_indices[-1]
while index != -1:
    lis.append(l[index])
    index = parent[index]
lis.reverse()  # LIS를 올바른 순서로 재배열

print(len(lis))
print(*lis)