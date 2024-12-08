import sys
input = sys.stdin.readline

n,m = map(int,input().split())
y,x,d = map(int,input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int,input().split())))
dx = (0,1,0,-1)
dy = (-1,0,1,0)
cnt = 0

while True:
    if matrix[y][x] == 0: ## 청소안돼있으면
        matrix[y][x] = 2 ## 청소
        cnt += 1

    check = [False if matrix[y+dy[i]][x+dx[i]] == 0 else True for i in range(4)] # 청소안된 곳만 False
    if all(check): # 사방에 청소안된 곳이 없으면
        backward = (d+2)%4 # 후진방향
        if matrix[y+dy[backward]][x+dx[backward]] == 1: # 뒤가 벽이면
            break
        else:
            y,x = y+dy[backward], x+dx[backward] # 후진
    else:
        d = (d+3)%4 # 반시계 방향 회전
        if matrix[y+dy[d]][x+dx[d]] == 0:
            y,x = y+dy[d], x+dx[d]

print(cnt)