from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

def snake(r,c):
    q = deque()
    q.append([r,c])
    board[r][c] = 2
    delta = {
        'D' : [0, 1, 0, -1],
        'L' : [1, 0, -1, 0]
    }
    direction = 0
    cnt = 1

    for i in range(K):
        n, D = moving[i][0], moving[i][1]
        for i in range(n):
            nr, nc = r+d[0], c+d[1]
            if 1<=nr<N and 1<=nc<N and board[nr][nc] != 2:
                q.append([nr,nc])
                cnt+=1
                # 빈칸이라면
                if not board[nr][nc]:
                    dr, dc = q.popleft()
                    board[dr][dc] = 0
                    board[nr][nc] = 2
                # 사과일 때
                elif board[nr][nc] == 1:
                    board[nr][nc] = 2
            else:
                return cnt
        d[0], d[1] = delta[D][1], delta[D][0]

N = int(input())
K = int(input())

board = [[0]*(N+1) for _ in range(N+1)]
for i in range(K):
    r,c = map(int, input().split())
    board[r][c] = 1

S = int(input())
moving = []
for i in range(S):
    m, d = input().split()
    moving.append([int(m), d])

print(snake(1,1))