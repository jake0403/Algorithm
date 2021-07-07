def dfs(r,c,s):
    if len(s) == 7:
        result.add(s)
        return
    for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        nr = r + dr
        nc = c + dc
        if 0<= nr < 4 and 0<= nc < 4:
            dfs(nr,nc,s+arr[nr][nc])



T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    result = set()
    for r in range(4):
        for c in range(4):
            dfs(r,c, arr[r][c])
    print(f'#{tc} {len(result)}')
