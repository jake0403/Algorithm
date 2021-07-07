from collections import deque
def bfs(n,m):
    q = deque([n])
    visited = [0] * 1000001
    visited[n] = 0
    while q:
        s = q.popleft()
        for cal in [s+1,s-1,s*2,s-10]:
            if cal == m:
                visited[cal] = visited[s]+1
                return visited[cal]
            if 0 <= cal < 1000000 and not visited[cal]:
                visited[cal] = visited[s]+1
                q.append(cal)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{tc} {bfs(N,M)}')
