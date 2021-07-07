from collections import deque
N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
si, sj = 0 , 0
visited[0][0] = 1
queue = deque([])
queue.append([si, sj])
while queue:
    i, j = queue.popleft()
    for di, dj in [(1,0),(0,1), (-1,0), (0,-1)]:
        ni = i + di
        nj = j + dj
        if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == 1 and visited[ni][nj] ==0:
            visited[ni][nj] = 1 + visited[i][j]
            queue.append([ni,nj])
            if ni == N-1 and nj == M-1:
                print(visited[ni][nj])
                break