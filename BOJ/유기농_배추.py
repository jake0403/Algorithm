def dfs(r,c):
    global ground
    ground[r][c]+=1
    for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
        nr, nc = r+dr, c+dc
        if 0<=nr<n and 0<=nc<m and ground[nr][nc] == 1:
            dfs(nr,nc)

T = int(input())
for tc in range(T):
    n,m,p = map(int,input().split())
    ground = [[0]*m for _ in range(n)]
    for _ in range(p):
        r,c = map(int,input().split())
        ground[r][c] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if ground[i][j] == 1:
                dfs(i,j)
                cnt+=1
    print(cnt)