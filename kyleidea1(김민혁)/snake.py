import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
k = int(input())
apple_pos = []
for _ in range(k):
    y,x = map(int,input().split())
    apple_pos.append((y,x))
l = []
t = int(input())
for _ in range(t):
    m,c = input().split()
    m = int(m)
    l.append((m,c))
dy = [-1,0,1,0]
dx = [0,1,0,-1]
d = 1 # 처음에는 오른쪽을 봄

matrix = [[0]*n for _ in range(n)]
for i in range(k):
    ay,ax = apple_pos[i]
    matrix[ay-1][ax-1] = 1 # 사과를 1로 두기
matrix[0][0] = 2 # 뱀 몸을 2로 두기
hy,hx,ty,tx = 0,0,0,0
s = 0 # 초 정보
s_idx = 0
snake = deque([(0,0)])

while True:
    s += 1

    hy,hx = hy+dy[d], hx+dx[d] # 보는 방향으로 한 칸 앞
    if hy<0 or hx < 0 or hy >= n or hx >= n or matrix[hy][hx] == 2:
        break
    
    if matrix[hy][hx] == 0: # 사과가 없는 빈 칸이면
        ty,tx = snake.popleft()
        matrix[ty][tx] = 0 # 꼬리 이동

    matrix[hy][hx] = 2
    snake.append((hy,hx))
    
    if s == l[s_idx][0]:
        if l[s_idx][1] == 'L':
            d = (d+3)%4
        elif l[s_idx][1] == 'D':
            d = (d+1)%4
        if s_idx < len(l)-1:
            s_idx += 1
    # 사과를 먹었으면 꼬리에는 아무 처리를 안 해도 됨
print(s)