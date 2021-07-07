# 익은 토마토 = 1, 익지 않은 토마토 = 0, 토마토가 없는 칸 = -1
import sys
from collections import deque
dr = [1,-1, 0,0,0,0]
dc = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def ripe():
    while q:
        z,r,c = q.popleft()
        visited[z][r][c] = 1
        for i in range(6):
            nz, nr, nc = z + dz[i], r + dr[i], c + dc[i]
            if 0<=nz<h and 0<=nr<n and 0<=nc<m and boxes[nz][nr][nc] == 0 and not visited[nz][nr][nc]:
                q.append([nz,nr,nc])
                visited[nz][nr][nc] = 1
                boxes[nz][nr][nc] = boxes[z][r][c] + 1

def find_unripe():
    for i in range(h):
        for j in range(n):
            # 하나라도 안 익은 토마토가 있으면 찾음
            if 0 in boxes[i][j]:
                return 1
    return 0


def solution():
    tomato_cnt = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if boxes[i][j][k] == 1:
                    q.append([i, j, k])
                # 토마토가 모두 익어있는 상태인지 확인
                elif boxes[i][j][k] == 0:
                    tomato_cnt+=1
    # 토마토가 모두 익어있는 상태라면 return 0
    if not tomato_cnt:
        return 0
    max_date = 0
    ripe()
    if find_unripe():
        return -1
    for i in range(h):
        for j in range(n):
            max_date = max(max_date, max(boxes[i][j]))
    return max_date-1

input = sys.stdin.readline
m,n,h = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
q = deque()
answer = solution()
print(answer)