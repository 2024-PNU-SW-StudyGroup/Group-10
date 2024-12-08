import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = []

for _ in range(n):
    matrix.append(list(map(int,input().split())))

def place_one(matrix):
    place_of_zeros = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                place_of_zeros.append((i,j))
    return place_of_zeros

def find_two(matrix):
    two_list = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 2:
                two_list.append((i,j))
    return two_list
            
def bfs(matrix,wall,two):
    for wx,wy in wall:
        matrix[wx][wy] = 1
    for tx,ty in two:
        q = deque((tx,ty))
        visit = [[False]*m for _ in range(n)]
        dx = (-1,1,0,0)
        dy = (0,0,-1,1)
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if 
            



