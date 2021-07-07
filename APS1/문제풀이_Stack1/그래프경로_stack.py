def stack_dfs(start, end, graph):
    visited = [0]*V
    stack = [start]

    while stack:
        # stack에 있는 값을 계속 꺼내고 넣고 하면서
        # 연결된 노드와 end 값 비교
        p = stack.pop()
        # 방문한 노드는 체크
        visited[p] = 1
        if end in graph[p]:
            return 1
        for i in graph[p]:
            if visited[i] == 0:
                stack.append(i)
    return 0

T = int(input())
for tc in range(1, T+1):
    V , E = map(int, input().split())
    graph = [[] for _ in range(V)]
    for i in range(E):
        fow, to = map(int, input().split())
        # 출발 노드가 어떤 노드에 도착하는지 기록
        graph[fow].append(to)
    # 출발 노드와 도착 노드 지정
    start, end = map(int, input().split())
    print(f'#{tc} {stack_dfs(start, end, graph)}')