from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

def bfs(sn):
    q = deque()
    q.append(sn)
    visited = [0]*(V+1)
    visited[sn] = 1
    cnt = 0
    while q:
        n = q.popleft()
        cnt+=1
        for v in graph[n]:
            if not visited[v]:
                q.append(v)
                visited[v] = 1
    return cnt




V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for i in range(E):
    sn, en = map(int, input().split())
    graph[en].append(sn)
max_trust = 0
ans = []
for i in range(1, V+1):
    if graph[i]:
        trust = bfs(i)
        if max_trust <= trust:
            if max_trust<trust:
                ans = []
                max_trust = trust
            ans.append(i)
print(*ans)