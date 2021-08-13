from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

def snake(r,c):
    q = deque()
    q.append([r,c])
    board[r][c] = 2
    delta = [(0,1),(1,0),(0,-1),(-1,0)]
    cnt = 1
    d = 0
    while True:
        nr, nc = r + delta[d][0], c + delta[d][1]
        if 1<= nr <=N and 1<= nc <N and board[nr][nc] != 2:
            if board[nr][nc] == 0:
                r, c = q.popleft()
                board[r][c] = 0
            board[nr][nc] = 2
            q.append([nr,nc])
            if cnt in moving:
                if moving[cnt] == 'L':
                    if d == 0:
                        d = 3
                    else:
                        d-=1
                else:
                    if d == 3:
                        d = 0
                    else:
                        d+=1
            cnt+=1
        else:
            return cnt
        r, c = nr, nc


N = int(input())
K = int(input())

board = [[0]*(N+1) for _ in range(N+1)]
for i in range(K):
    r,c = map(int, input().split())
    board[r][c] = 1

L = int(input())
moving = {}
for i in range(L):
    m, d = input().split()
    moving[int(m)] = d

print(snake(1,1))