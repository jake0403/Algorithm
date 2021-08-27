from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

def bfs(q):
    while q:
        r1,c1, r2,c2, cnt = q.popleft()

        if cnt >= 10:
            return -1
        for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            nr1, nc1 = r1 + dr, c1 + dc
            nr2, nc2 = r2 + dr, c2 + dc
            if 0 <= nr1 < n and 0 <= nc1 < m and 0<= nr2 < n and 0<=nc2<m:
                if board[nr1][nc1] == '#':
                    nr1, nc1 = r1, c1
                if board[nr2][nc2] == '#':
                    nr2, nc2 = r2, c2
                q.append([nr1,nc1,nr2,nc2,cnt+1])
            elif 0<= nr1 < n and 0<= nc1 < m :
                return cnt + 1
            elif 0<=nr2<n and 0<= nc2 <m :
                return cnt+1
            else:
                continue




n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
ball = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 'o':
            ball.append([i,j])
q = deque()
q.append([ball[0][0], ball[0][1], ball[1][0], ball[1][1], 0])
print(bfs(q))