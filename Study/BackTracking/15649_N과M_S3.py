import sys
input = lambda : sys.stdin.readline().strip()

N, C = map(int, input().split())
visited = [0]*(N+1)
def dfs(ans):
    if len(ans) > C:
        return
    if len(ans) == C:
        print(" ".join(map(str,ans)))
        return
    for i in range(1,N+1):
        if not visited[i]:
            ans.append(i)
            visited[i] = 1
            dfs(ans)
            visited[i] = 0
            ans.pop()

dfs([])