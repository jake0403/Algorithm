def dfs(s,e):
    global visited, answer
    if s == e:
        answer = 1
        return answer
    if not visited[s] and graph[s]:
        visited[s] = 1
        for n in graph[s]:
            dfs(n,e)
    return answer
T = int(input())
for tc in range(1, T+1):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    for i in range(e):
        p,c = map(int,input().split())
        graph[p]+= [c]
    sn, en = map(int,input().split())
    visited = [0]*(v+1)
    answer = 0
    dfs(sn,en)
    print(f'#{tc} {answer}')