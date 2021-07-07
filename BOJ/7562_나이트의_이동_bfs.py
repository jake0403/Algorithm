import sys
from collections import deque
input = sys.stdin.readline

def bfs(sr,sc):
    q = deque([[sr, sc]])
    while q:
        r,c = q.popleft()
        for dr, dc in [(-2,1),(-1,2), (1,2),(2,1), (2,-1),(1,-2), (-1,-2),(-2,-1) ]:
            nr, nc = r+dr, c+dc
            # 체스판 범위를 넘지 않고 방문하지 않았거나 목적지라면
            if 0<=nr<N and 0<=nc<N and (arr[nr][nc] == 0 or arr[nr][nc] == 'A'):
                if arr[nr][nc] == 'A':
                    return arr[r][c]+1
                arr[nr][nc] = arr[r][c]+1
                q.append([nr,nc])


T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    sr, sc = map(int, input().split())
    er, ec = map(int, input().split())
    if sr == er and sc == ec:
        print(0)
        continue
    arr[sr][sc] = 1
    arr[er][ec] = 'A'
    print(bfs(sr,sc)-1)
