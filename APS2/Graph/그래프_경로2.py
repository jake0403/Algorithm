from collections import deque
def GR(sV, eV):
    visited = [0]*(V+1)
    q = deque([sV])
    visited[sV] = 1

    while q:
        node = q.popleft()
        if node == eV:
            return 1
        for i in range(1,V+1):
            if adj[node][i] and not visited[i]:
                q.append(i)
                visited[i] = 1
    return 0
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        s,e = map(int, input().split())
        adj[s][e] = 1
    startV, endV = map(int, input().split())
    print(f'#{tc} {GR(startV,endV)}')
