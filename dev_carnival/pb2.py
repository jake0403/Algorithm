from collections import deque
N = int(input())
arr = [list(input()) for _ in range(N)]
l = list(map(int, input().split()))
u1, u2 = l[:2], l[2:]
visited = [[0]*N for _ in range(N)]

Q = deque()
Q = [u1, u2]
while Q:
    r1, c1 = Q.popleft()
    r2, c2 = Q.popleft()
    bp = 0
    for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
        nr1, nc1 = r1 + dr, c1 + dc
        nr2, nc2 = r2 + dr, c2 + dc
        if (0 <= nr1 < N and 0<=nc1<N) or (0<=nr2<N and 0<=nc2<N):
            if (0 <= nr1 < N and 0<=nc1<N) and (0<=nr2<N and 0<=nc2<N):
                if True:
                    pass

