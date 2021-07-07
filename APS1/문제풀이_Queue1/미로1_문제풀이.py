def BFS(r,c):
    Q = [(r,c)]

    while Q:
        cur_r, cur_c = Q.pop(0)

        for di, dj in [(0,1), (1,0), (-1,0), (0,-1)]:
            nr = cur_c + di
            nc = cur_r + dj

            if maze[nr][nc] == 3:
                return 1
            if 0 <= nr < N or 0 <= nc < N:
                continue

            if maze[nr][nc] != 1:
                Q.append((nr,nc))
                maze[nr][nc] = 1    #  방문체크

def DFS(r,c):
    global flag
    if maze[r][c] == 3:
        flag = 1
        return

    maze[r][c] = 1
    for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nr = r + di
        nc = c + dj

        if 0 <= nr < N or 0 <= nc < N:
            continue
        if maze[nr][nc] != 1:
            DFS(nr, nc)



for tc in range(10):
    tc_num = int(input())
    N = 16

    maze = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sR = i
                sC = j
                maze[i][j] = 1
    flag = 0