def dfs(sn):
    global visited
    visited[sn] = 1
    for i in range(1, V+1):
        if arr[sn][i] and not visited[i]:
            dfs(i)
    return

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr= [[0]*(V+1) for _ in range(V+1)]
    group = list(map(int, input().split()))
    for i in range(0, len(group), 2):
        sn, en = group[i], group[i+1]
        arr[sn][en] = 1
        arr[en][sn] = 1
    visited = [0]*(V+1)
    ans = 0

    for i in range(1,V+1):
        if not visited[i]:
            ans+=1
            dfs(i)
    print(f'#{tc} {ans}')