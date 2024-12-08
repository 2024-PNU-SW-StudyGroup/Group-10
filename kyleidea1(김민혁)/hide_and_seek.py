from collections import deque

n, k = map(int,input().split())

q = deque([n])
visited = [False] * 200002

cnt = 0
while q:
    found = False
    for _ in range(len(q)):
        x = q.popleft()
        if x == k:
            found = True
            break
        elif x <= 100001:
            if not visited[x-1]:
                q.append(x-1)
                visited[x-1] = True
            if not visited[x+1]:
                q.append(x+1)
                visited[x+1] = True
            if not visited[2*x]:
                q.append(2*x)
                visited[2*x] = True
    if found:
        break
    else:
        cnt += 1
print(cnt)