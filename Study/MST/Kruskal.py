V, E = map(int, input().split())
edge = []
parent = [i for i in range(V+1)]
for _ in range(E):
    u, v, w = map(int,input().split())
    edge.append((w,u,v))

edge.sort()

def findSet(x):
    while x != parent[x]:
        x = parent[x]
    return x

total = 0
N = V+1
cnt = 0

for w, u, v in edge:
    repU = findSet(u)
    repV = findSet(v)
    if repU != repV:
        cnt+=1
        total += w
        parent[repV] = repU
        if cnt == N-1:
            break
print(total)