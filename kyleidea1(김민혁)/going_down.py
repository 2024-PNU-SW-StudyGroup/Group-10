n = int(input())
dp = [[i,i] for i in list(map(int, input().split()))]

for _ in range(1, n):
    temp = list(map(int, input().split()))
    dp[0][0], dp[0][1], dp[1][0], dp[1][1], dp[2][0], dp[2][1] = max(dp[0][0] + temp[0], dp[1][0] + temp[0]), min(dp[0][1] + temp[0], dp[1][1] + temp[0]), max(dp[0][0] + temp[1], dp[1][0] + temp[1], dp[2][0] + temp[1]), min(dp[0][1] + temp[1], dp[1][1] + temp[1], dp[2][1] + temp[1]), max(dp[1][0] + temp[2], dp[2][0] + temp[2]), min(dp[1][1] + temp[2], dp[2][1] + temp[2])

print(max([i[0] for i in dp]), min([i[1] for i in dp]))