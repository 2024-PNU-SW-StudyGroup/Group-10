x = int(input())
l = []
R,G,B = [],[],[]
for _ in range(x):
    r,g,b = map(int,input().split())
    R.append(r)
    G.append(g)
    B.append(b)

for i in range(1,x):
    R[i] = min(R[i] + G[i-1], R[i] + B[i-1])
    G[i] = min(G[i] + R[i-1], G[i] + B[i-1])
    B[i] = min(B[i] + R[i-1], B[i] + G[i-1])

print(min(R[x-1],G[x-1],B[x-1]))
