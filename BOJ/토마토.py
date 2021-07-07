from collections import deque
def bfs(ripe):
    q = deque(ripe)
    max_date = 0
    while q:
        r,c = q.popleft()
        for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<m and 0<=nc<n and box[nr][nc] == 0:
                q.append([nr,nc])
                box[nr][nc]=box[r][c]+1
                max_date = max(max_date, box[nr][nc])
    if max_date == 0:
        max_date = 1
    return max_date-1
n,m = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(m)]
ripe = []
for i in range(m):
    for j in range(n):
        if box[i][j] == 1:
            ripe.append([i,j])
ans = bfs(ripe)
for b in box:
    if 0 in b:
        ans = -1
        break
print(ans)