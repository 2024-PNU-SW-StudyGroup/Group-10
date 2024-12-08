import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


m,n = map(int, input().split())
matrix = [list(input()) for _ in range(m)]
visited = [0]*26
visited[ord(matrix[0][0])-ord('A')] = True

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y,cnt):
    global ans
    ans = max(ans, cnt)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if not visited[ord(matrix[nx][ny])-ord('A')]:
            visited[ord(matrix[nx][ny])-ord('A')] = True
            dfs(nx,ny,cnt+1)
            visited[ord(matrix[nx][ny])-ord('A')] = False

ans = 1
dfs(0,0,1)
print(ans)

# 이 문제 어렵다..
# 어려운 이유 1: dfs를 명시적 스택으로 써서 구현해왔는데, 그렇게 되면 복귀 시 방문처리 회수가 안 됨.
# 어려운 이유 2: 지금까지의 방문한 서로 다른 알파벳 수를 상태에 추가해야 함.
# 결론: 재귀 dfs를 적극적으로 쓰자!
