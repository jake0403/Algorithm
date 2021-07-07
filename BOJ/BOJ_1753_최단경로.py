from collections import deque
def bfs(s):
    q = deque()
    q.append(s)
    visited = [-1] * (v + 1)
    visited[startV] = 0
    while q:
        s = q.popleft()
        for i in range(1, v+1):
            if adj[s][i] != 0 and visited[i] == -1 :
                q.append(i)
                visited[i] =  adj[s][i] + visited[s]

    return visited




v, e = map(int, input().split())
startV = int(input())
adj = [[0]*(v+1) for _ in range(v+1)]
for i in range(v+1):
    u, z, w = map(int,input().split())
    adj[u][z] = w
route = bfs(startV)
for i in range(1,v+1):
    print(route[i]) if route[i] != -1 else print('INF')

