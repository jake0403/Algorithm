from collections import deque
import sys
input = sys.stdin.readline

def bfs(sr,sc, cnt):
    q = deque([[sr,sc]])
    while q:
        r,c = q.popleft()
        for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0<=nr<M and 0<=nc<N and arr[nr][nc] == 0:
                q.append([nr,nc])
                arr[nr][nc] =2
                cnt+=1
    return cnt

M, N, K = map(int, input().split())
arr = [[0]*(N) for _ in range(M)]
answer = []
for i in range(K):
    dot = list(map(int, input().split()))
    for j in range(dot[1], dot[3]):
        for k in range(dot[0], dot[2]):
            if not arr[j][k]:
                arr[j][k] = 1

for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            arr[i][j] = 2
            answer.append(bfs(i,j,1))
answer.sort()
print(len(answer))
for a in answer:
    print(a, end=' ')
