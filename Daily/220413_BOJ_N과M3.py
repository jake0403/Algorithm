N, R = map(int, input().split())
arr = list(range(1,N+1))
permu = []
visited = [0]*N
def dfs(per):
    global visited
    if len(per) == R:
        print(' '.join(map(str, per)))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            per.append(arr[i])
            dfs(per)
            per.pop()
            visited[i] = 0


dfs([])
