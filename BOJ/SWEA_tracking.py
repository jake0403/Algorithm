def bfs(i,j):
    pass

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    track = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    max_height = 0
    for i in range(N):
        max_height = max(max_height, max(track[i]))

    for i in range(N):
        for j in range(N):
            if track[i][j] == max_height:
                bfs(i,j)