import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
for i in range(1,N):
    maze[i][0] += maze[i-1][0]
for j in range(1,M):
    maze[0][j] += maze[0][j-1]

for i in range(1, N):
    for j in range(1,M):
        maze[i][j]+= max(maze[i-1][j-1], maze[i][j-1], maze[i-1][j])
print(maze[N-1][M-1])