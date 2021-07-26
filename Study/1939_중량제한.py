import sys
from collections import deque
input = sys.stdin.readline

def bfs(c):
    q = deque()
    q.append(start)
    visited = [0]*(N+1)
    visited[start] = 1

    while q:
        a = q.popleft()
        for b, w in adj[a]:
            if not visited[b] and w >= c:
                visited[b] = 1
                q.append(b)
    return True if visited[end] else False


N, M = map(int, input().split())
maxW, minW = 0, 1
adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    maxW = max(maxW, w)
    adj[s].append((e,w))
    adj[e].append((s,w))
start, end = map(int, input().split())

answer = 0

# 이진 탐색하며 최대 옮길 수 있는 용량 찾기
while minW <= maxW:
    mid = (minW + maxW) //2
    if bfs(mid):
        answer = mid
        minW = mid+1
    else:
        maxW = mid-1

print(answer)
