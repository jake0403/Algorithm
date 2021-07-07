from collections import deque
def bfs(r,c,m):
    q = deque([[r,c]])
    m[r][c] = 1
    while q:
        r, c = q.popleft()
        for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < 100 and 0 <= nc < 100 and m[nr][nc] != 1:
                if m[nr][nc] == 3:
                    return 1
                q.append([nr,nc])
                m[nr][nc] = 1
    return 0

def dfs(r,c):
    global flag, maze
    if maze[r][c] == 1:
        return
    maze=[r][c] = 1
    for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
        nr = r + dr
        nc = c + dc
        if 0<= nr < 100 and 0<= nc < 100 and maze[nr][nc] != 1:
            if maze[nr][nc] == 3:
                flag = 1
                return
            dfs(nr,nc)

for tc in range(1, 11):
    n = input()
    maze = [list(map(int, input())) for _ in range(100)]
    sr, sc = 1, 1
    flag = 0
    dfs(sr,sc)
    # print('#{} {}'.format(tc, bfs(sr,sc,maze)))
    print(f'#{tc} {dfs(sr,sc)}')