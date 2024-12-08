n=int(input())%((15)*(10**5))
dp=[_ for _ in range(n+1)]
for i in range(2,n+1):
    dp[i]=(dp[i-2]+dp[i-1])%1000000
print(dp[n])
