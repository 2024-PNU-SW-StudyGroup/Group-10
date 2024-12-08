from collections import deque

def bfs():
    start, target = map(str, input().split())
    visited = set([])
    q = deque()

    q.append(start)
    visited.add(start)

    cnt = 0
    while q:
        cnt += 1
        for _ in range(len(q)):
            v = q.popleft()
            if v == target:
                return cnt
            else:
                if str(int(v)*2) not in visited and len(str(int(v)*2)) <= len(target):
                    q.append(str(int(v)*2))
                    visited.add(str(int(v)*2))
                if v+'1' not in visited and len(v+'1') <= len(target):
                    q.append(v+'1')
                    visited.add(v+'1')
    return -1

print(bfs())