import sys
input = sys.stdin.readline

def dfs(r,c,move,pb):
    global answer

    if N == move:
        answer += pb

    for i, [dr, dc] in enumerate([(0,1), (0,-1), (1,0), (-1,0)]):
        nr = r + dr
        nc = c + dc

        if 0<= nr < (2*N+1) and 0<= nc < (2*N+1) and board[nr][nc] == 0:
            board[nr][nc] = 1
            dfs(nr, nc, move+1, pb * percent[i] * 0.01)
            board[nr][nc] = 0


N, East, West, South, North = map(int, input().split())
percent = [East, West, South, North]

board = [[0]*(2*N+1) for _ in range(2*N+1)]
board[N][N] = 1
answer = 0

dfs(N,N,0,1)
print(answer)