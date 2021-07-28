import sys
from collections import deque
input = sys.stdin.readline

def bfs(r,c):
    q = deque()
    q.append([r,c])
    arr[r][c] = 0
    ans = 1
    while q:
        r,c = q.popleft()
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r+dr, c+dc
            if 0<= nr< n and 0<= nc <m and arr[nr][nc] == 1:
                arr[nr][nc] = 0
                ans+=1
                q.append([nr,nc])
    return ans



n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            answer.append(bfs(i,j))
if answer:
    print(len(answer))
    print(max(answer))
else:
    print(0)
    print(0)