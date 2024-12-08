import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution(w,h):
    matrix = [[] for _ in range(h)]
    for i in range(h):
        tmp = list(map(int, input().split()))
        matrix[i] = tmp

    dx = [1,1,1,0,-1,-1,-1,0]
    dy = [1,0,-1,-1,-1,0,1,1]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                stack = [(i,j)]
                while stack:
                    x,y = stack.pop()
                    for k in range(8):
                        nx, ny = x + dx[k], y + dy[k]
                        if nx < 0 or ny < 0 or nx >= h or ny >= w:
                            continue
                        if matrix[nx][ny] == 1:
                            stack.append((nx,ny))
                            matrix[nx][ny] = 0
                cnt += 1
    return cnt

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        print(solution(w,h))