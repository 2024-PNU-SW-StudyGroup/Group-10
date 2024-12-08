import sys

T = int(sys.stdin.readline())

input_list = []
for _ in range(T):
    t = int(sys.stdin.readline())
    input_list.append(t)

dp = [0] * (max(input_list)+1)

dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4,T+1):
    dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

print(dp)
    
