T = int(input())
def dfs(v, end, num_list, visited):
    visited[v] = 1
    # 출발하고자 하는 노드가 end 노드라면 return
    if v== end:
        return 1
    # 시작 노드가 방문한 노드들을 반복하며 재귀
    for i in num_list[v]:
        if visited[i] == 0:
            result = dfs(i, end, num_list, visited)
            if result == 1:
                return result
    return 0


for tc in range(1, T+1):
    V, E = map(int,input().split())
    # 시작 노드가 fan out 되는 노드들 저장
    graph = [[] for x in range(V+1)]
    visited = [0] * len(graph)
    # 간선 횟수만큼 반복
    for i in range(E):
        # 출발 노드 도착 노드들 나눠서 저장
        fow , to = map(int,input().split())
        graph[fow].append(to)
    start_V , end_V = map(int, input().split())
    print(graph)
    print('#{} {}'.format(tc, dfs(start_V,end_V,graph, visited)))
