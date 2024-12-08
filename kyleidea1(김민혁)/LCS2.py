import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

def get_LCS(a,b):
    dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
    
    LCS = ''
    x,y = len(a),len(b)
    while x != 0 and y != 0:
        if dp[x][y] == dp[x-1][y]:
            x = x-1
        elif dp[x][y] == dp[x][y-1]:
            y = y-1
        else:
            x,y = x-1, y-1
            LCS += a[x]
    return LCS[::-1]

LCS = get_LCS(a,b)
print(len(LCS))
print(LCS)