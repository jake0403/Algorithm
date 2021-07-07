from collections import deque
def bfs(i,j):
    queue = deque()
    queue.append([i,j])
    visited[i][j] = 1

    while queue:
        i, j = queue.popleft()
        for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and rgb[ni][nj] == rgb[i][j]:
                queue.append([ni, nj])
                visited[ni][nj] = 1
N = int(input())
rgb = [list(input()) for _ in range(N)]
cnt = 0
visited = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i,j)
            cnt+=1
print(cnt)