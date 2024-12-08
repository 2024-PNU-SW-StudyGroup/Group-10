import sys
input = sys.stdin.readline

n = int(input())
lis = list(map(int,input().split()))
target = int(input())
lis.sort() # 핵심!

l = 0
r = n-1
cnt = 0

while l < r:
    cur_sum = lis[l] + lis[r]
    if cur_sum == target:
        cnt += 1
        l += 1
        r -= 1
    elif cur_sum < target:
        l += 1
    else:
        r -= 1

print(cnt)