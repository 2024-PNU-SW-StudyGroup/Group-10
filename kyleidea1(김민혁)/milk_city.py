import sys
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int,input().strip().split())) for _ in range(n)]
prev = [[-1]*n for _ in range(n)]
dp = [[0]*(n) for _ in range(n)]

print(prev)

def okay(cur, prev):
    return (cur == 1 and prev == 0) or (cur == 2 and prev == 1) or (cur == 0 and prev == 2)

for i in range(n):
    for j in range(n):
        if i<0 or j<0:
            continue
        if okay(matrix[i][j],prev[i-1][j]) and okay(matrix[i][j],prev[i][j-1]):
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            prev[i][j] = matrix[i-1][j]
        elif okay(matrix[i][j],prev[i-1][j]):
            if dp[i-1][j]+1 > dp[i][j-1]
            dp[i][j] = max(dp[i-1][j]+1,dp[i][j-1])
            prev = 
        

            
            