import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    visited = [[0] * M for _ in range(N)]
    q = deque([[0,0]])
    # 판의 가장자리는 치즈가 없으므로 0,0 부터 시작
    visited[0][0] = 1
    cnt = 0
    while q:
        r,c = q.popleft()
        for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            nr, nc = r + dr, c + dc
            if 0<=nr<N and 0<=nc<M and visited[nr][nc] == 0:
                if arr[nr][nc] == 0:
                    q.append([nr,nc])
                    visited[nr][nc] = 1
                elif arr[nr][nc] == 1:
                    arr[nr][nc] = 0
                    visited[nr][nc] = 1
                    cnt+=1
    cheese.append(cnt)
    return cnt




N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cheese = []
hour = 0
while True:
    cnt = bfs()
    if cnt == 0:
        break
    hour+=1
print(hour)
print(cheese[-2])