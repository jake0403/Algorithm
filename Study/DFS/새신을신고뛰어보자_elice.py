from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

def bfs(r,c):
    q = deque()
    q.append((r,c))
    ans = 0
    while q:
        r,c = q.popleft()
        for dr, dc in [(0, arr[r][c]), (arr[r][c], 0)]:
            nr, nc = r+dr, c + dc
            if 0<=nr < N and 0<=nc <N:
                if arr[nr][nc] == 0:
                    ans +=1
                else:
                    q.append((nr, nc))
    return ans

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = bfs(0,0)
print(ans)