import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()
c = input().strip()

dp = [[[0]*(len(c)+1) for _ in range(len(b)+1)] for _ in range(len(a)+1)]

ans = 0
for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(c)):
            if a[i] == b[j] == c[k]:
                dp[i+1][j+1][k+1] = dp[i][j][k] + 1
            else:
                dp[i+1][j+1][k+1] = max(dp[i][j+1][k+1],dp[i+1][j][k+1],dp[i+1][j+1][k])
        if dp[i+1][j+1][k+1] >= ans:
                ans = dp[i+1][j+1][k+1]

print(ans)

# def get_LCS(a,b):
#     dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
#     for i in range(len(a)):
#         for j in range(len(b)):
#             if a[i] == b[j]:
#                 dp[i+1][j+1] = dp[i][j] + 1
#             else:
#                 dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
    
#     LCS = ''
#     x,y = len(a),len(b)
#     while x != 0 and y != 0: # 중요
#         if dp[x][y] == dp[x-1][y]:
#             x = x-1
#         elif dp[x][y] == dp[x][y-1]:
#             y = y-1
#         else:
#             x,y = x-1, y-1
#             LCS += a[x]
#     return LCS[::-1]

# LCS_ab = get_LCS(a,b)
# LCS_bc = get_LCS(b,c)
# LCS_ac = get_LCS(a,c)

# ans = max(len(get_LCS(LCS_ab,c)),len(get_LCS(LCS_bc,a)),len(get_LCS(LCS_ac,b)))
# print(ans)