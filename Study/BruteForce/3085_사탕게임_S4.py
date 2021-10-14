import sys
input = lambda : sys.stdin.readline().strip()

N = int(input())
board = [list(input()) for _ in range(N)]
max_candy = 0

def check():
    global max_candy
    for i in range(N):
        candyR = candyC = 1
        for j in range(N-1):
            if board[i][j] == board[i][j+1]:
                candyR+=1
            else:
                max_candy = max(max_candy, candyR)
                candyR = 1
            if board[j][i] == board[j+1][i]:
                candyC+=1
            else:
                max_candy = max(max_candy, candyC)
                candyC = 1
    max_candy = max(max_candy, candyC, candyR)


for i in range(N):
    for j in range(N-1):
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        check()
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
for i in range(N):
    for j in range(N-1):
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
        check()
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

print(max_candy)