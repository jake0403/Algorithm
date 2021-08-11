from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

def snake():
    global q
    delta = {
        "D": [0,1],
        "L": [0,-1]
    }
    r = c = 1
    board[r][c] = 1
    q.append([1,1])
    dm = [0,1]
    cnt = 1
    for m in moving:
        n, d = int(m[0]), m[1]
        for i in range(n):
            nr, nc = r+dm[0], c+dm[1]
            if 0 < nr <= N and 0 < nc <= N and (not board[nr][nc] or board[nr][nc] == "A"):
                q.append([nr,nc])
                cnt+=1
                # 뱀이 다음으로 갈 곳이 사과라면
                if board[nr][nc] == "A":
                    board[nr][nc] = board[r][c]
                    board[nr][nc]+=1
                # 뱀이 다음으로 갈 곳이 빈 칸이라면
                else:
                    if q:
                        e, m = q.popleft()
                        board[e][m] = 0
            else:
                return cnt
            r,c = nr, nc
        delta[d][0], delta[d][1] = delta[d][1], delta[d][0]
        dm = [delta[d][0], delta[d][1]]

N = int(input())
# 사과 수, 위치 정보
A = int(input())
board = [[0]*(N+1) for _ in range(N+1)]
for a in range(A):
    a, p = map(int, input().split())
    board[a][p] = "A"

# 뱀이 몸이 있는 곳의 정보
visited = [[0]*(N+1) for _ in range(N+1)]

# 뱀의 이동횟수, 이동 정보
M = int(input())
moving = [list(input().split()) for _ in range(M)]

# 뱀의 몸 길이 정보
q = deque()
print(snake())
