def dfs_maze(i, j, N):
    if maze[i][j] == 3:
        return 1
    else:
        visited[i][j] = 1
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and visited[ni][nj] ==0:
                if dfs_maze(ni,nj,N):
                    return 1
        return 0

for t in range(1, 11):
    tc = int(input())
    N = 16
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    si, sj = 1 , 1

    print(f'#{tc} {dfs_maze(si,sj, N)}')