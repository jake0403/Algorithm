def bfs(s, e, V):
    queue = []
    visited = [0] * (V+1)
    queue.append(s)
    visited[s] = 1
    while queue:
        n = queue.pop(0)
        if n == e:
            return visited[n] - 1

        for i in range(1,V+1):
            if graph[n][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = 1 + visited[n]
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0]*(V+1) for _ in range(V+1)]
    # 무방향이므로 인접행렬 생성
    for i in range(E):
        fow, to = map(int, input().split())
        graph[fow][to]= 1
        graph[to][fow] = 1
    start_V , end_V = map(int,input().split())
    print(f'#{tc} {bfs(start_V, end_V, V)}')