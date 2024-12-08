n, m = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0
l = 0
cur_sum = 0
for r in range(n):
    cur_sum += num[r]
    while cur_sum > m and l <= r:
        cur_sum -= num[l]
        l += 1
    if cur_sum == m:
        cnt += 1
print(cnt)