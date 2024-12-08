from collections import deque

def dfs(graph, v, visited):
    visited[v] = True # 현재 노드를 방문 처리
    print(v, end = ' ')

    for i in graph[v]: # 그래프의 모든 노드들 중
        if not visited[i]: # 방문하지 않은 노드에 대해
            dfs(graph, i, visited) # 현재 노드를 방문 처리

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue: #큐가 빌 때 끝남!!
        v = queue.popleft() # 우선 젤 앞 놈 꺼내기(새로 너비탐색할 노드의 부모)
        for i in graph[v]: # 꺼낸 놈

