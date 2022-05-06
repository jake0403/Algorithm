import sys
input = lambda : sys.stdin.readline().strip()

def dfs(n,i):
    visited[n] = 1

    for v in arr[n]:
        if not visited[v]:
            dfs(v,i)
        elif visited[v] and v == i:
            answer.append(v)

N = int(input())
arr = [[] for _ in range(N+1)]

for i in range(1,N+1):
    arr[i].append(int(input()))
answer = []
for i in range(1,N+1):
    visited = [0]*(N+1)
    dfs(i,i)
print(len(answer))
print(*answer, sep='\n')
