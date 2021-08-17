from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

def bfs(r,c, sheep, wolf):
    q = deque()
    q.append([r,c])
    visited[r][c] = 1

    while q:
        r,c = q.popleft()
        for dr, dc in [(0,1),(1,0),(-1,0), (0,-1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr < N and 0<=nc <M and not visited[nr][nc] and arr[nr][nc] != '#':
                if arr[nr][nc] == "o":
                    sheep+=1
                elif arr[nr][nc] == 'v':
                    wolf+=1
                q.append([nr,nc])
                visited[nr][nc] = 1
    if sheep > wolf:
        return [sheep, 0]
    else:
        return [0, wolf]



N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
s_cnt = w_cnt = 0

for i in range(N):
    for j in range(M):
        s = w = 0
        if arr[i][j] != '#' and not visited[i][j]:
            if arr[i][j] == 'o':
                s = 1
            elif arr[i][j] == 'v':
                w = 1
            morning = bfs(i,j,s,w)
            s_cnt+=morning[0]
            w_cnt+=morning[1]
print(s_cnt, w_cnt)
