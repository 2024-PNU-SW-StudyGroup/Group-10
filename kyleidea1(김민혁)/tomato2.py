import sys
from collections import deque

input = sys.stdin.readline

def main():
    m,n,h = map(int, input().strip().split())
    matrix = [[list(map(int, input().strip().split())) for _ in range(n)] for _ in range(h)]

    def find_in_matrix(matrix, target):
        pos_list = []
        for i in range(h):
            for j in range(n):
                for k in range(m):
                    if matrix[i][j][k] == target:
                        pos_list.append((i,j,k))
        return pos_list

    mature = find_in_matrix(matrix,1)

    q = deque()
    visited = [[[False]*m for _ in range(n)] for _ in range(h)]

    for z,y,x in mature:
        q.append((z,y,x))
        visited[z][y][x] = True

    dx = [-1,1,0,0,0,0]
    dy = [0,0,-1,1,0,0]
    dz = [0,0,0,0,-1,1]

    cnt = 0
    while q:
        cnt += 1
        for _ in range(len(q)):
            z,y,x = q.popleft()
            for i in range(6):
                nz,ny,nx = z + dz[i], y + dy[i], x + dx[i]
                if nx<0 or nx>=m or ny<0 or ny>=n or nz<0 or nz>=h or matrix[nz][ny][nx] == -1:
                    continue
                if not visited[nz][ny][nx] and matrix[nz][ny][nx] == 0:
                    q.append((nz,ny,nx))
                    visited[nz][ny][nx] = True
                    matrix[nz][ny][nx] = 1

    print(cnt-1 if not find_in_matrix(matrix,0) else -1)

if __name__ == '__main__':
    main()