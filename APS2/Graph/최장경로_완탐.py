def dfs(start, cnt):
    global maxD
    if maxD < cnt:
        maxD = cnt

    for i in range(1, V+1):
        if graph[start][i] and not visited[i]:
            visited[i] = 1
            dfs(i, cnt+1)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    graph = [[0]*(V+1) for _ in range(V+1)]
    for i in range(E):
        sv, ev = map(int, input().split())
        graph[sv][ev] = 1
        graph[ev][sv] = 1
    maxD = 1
    # 왜 cnt 값을 변수로 안주고 밑에 함수에 인자로 주면 안되는지
    cnt = 1
    for i in range(1, V+1):
        visited = [0]*(V+1)
        visited[i] = 1
        dfs(i, cnt)
    print(f'#{tc} {maxD}')