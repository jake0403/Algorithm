from collections import deque
import sys

input = lambda: sys.stdin.readline().strip()
dr = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
dc = [0, 1, -1, 0, 1, -1, 0, 1, -1]


def fallingWall():
    for i in range(N - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = ['.', '.', '.', '.', '.', '.', '.', '.']


def maze(r, c):
    q = deque()
    q.append([r, c])
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            if arr[r][c] == '#':
                continue
            for i in range(9):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != '#':
                    if nr == 0 and nc == 7:
                        return 1
                    q.append([nr, nc])
        fallingWall()
    return 0


N = 8
arr = [list(input()) for _ in range(N)]
wall = []

print(maze(7, 0))