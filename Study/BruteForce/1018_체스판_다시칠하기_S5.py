import sys
input = lambda : sys.stdin.readline().strip()

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
min_check = sys.maxsize
for i in range(N-8+1):
    for j in range(M-8+1):
        check1 = 0
        check2 = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)% 2 == 0:
                    if board[k][l] != 'W': check1+=1
                    if board[k][l] != 'B': check2+=1
                else:
                    if board[k][l] != 'W': check2+=1
                    if board[k][l] != 'B': check1+=1
        min_check = min(check1, check2, min_check)
print(min_check)