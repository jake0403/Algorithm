from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

N, K = map(int, input().split())

time = [0] * 100001
route = [0] * 100001

def routeHistory(v):
    history = [v]
    T = time[v]
    for i in range(T):
        h = route[v]
        history.append(h)
        v = h
    print(' '.join(map(str, history[::-1])))

def bfs(N):
    q = deque()
    q.append(N)
    while q:
        v = q.popleft()
        if v == K:
            print(time[v])
            routeHistory(v)
            return
        for i in [v+1, v-1, v*2]:
            if 0 <= i < 100001 and time[i] == 0:
                time[i] = time[v] + 1
                route[i] = v
                q.append(i)

bfs(N)