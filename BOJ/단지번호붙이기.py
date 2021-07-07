from collections import deque
def bfs(r,c):
    global ans
    cnt = 1
    Q = [[r,c]]
    Q = deque(Q)
    arr[r][c] = 0
    while Q:
        r, c = Q.popleft()
        for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc]:
                cnt+=1
                arr[nr][nc] = 0
                Q.append([nr,nc])
    return cnt

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            ans.append(bfs(i,j))

ans.sort()
print(len(ans))
for a in ans:
    print(a)