import sys
input = lambda : sys.stdin.readline().strip()

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for i in range(1, N):
    num = int(input())
    nodes = list(map(int, input().split()))
    graph[i]+=nodes
flag = True
def dfs(s):
    global flag ,visited
    visited[s] = 1
    if s == N:
        return
    for g in graph[s]:
        if visited[g] == 1:
            flag = False
            return
        elif visited[g] == 0:
            dfs(g)
    visited[s] = -1

dfs(1)
if flag:
    print("NO CYCLE")
else:
    print("CYCLE")