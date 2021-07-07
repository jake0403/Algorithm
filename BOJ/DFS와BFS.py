def dfs(sn, visited):
    if len(visited) == V:
        return visited
    for i in range(1, V+1):
        if adj[sn][i] and i not in visited:
            visited.append(i)
            dfs(i, visited)
    return visited

from collections import deque
def bfs(sn):
    visited = [sn]
    q = deque([sn])
    while q:
        r = q.popleft()
        for c in range(V+1):
            if adj[r][c] and c not in visited:
                visited.append(c)
                q.append(c)
    return visited



V, E, sV = map(int, input().split())
adj = [[0]*(V+1) for _ in range(V+1)]
for _ in range(E):
    sn, en = map(int, input().split())
    adj[sn][en] = 1
    adj[en][sn] = 1
visited = [sV]
print(*dfs(sV,visited))
print(*bfs(sV))
