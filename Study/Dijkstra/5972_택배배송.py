import heapq
import sys

input = lambda : sys.stdin.readline().strip()

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    dist[start] = 0

    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for i in graph[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))


N,E = map(int, input().split())
graph = [[] for _ in range(N+1)]
INF = sys.maxsize
dist = [INF] * (N+1)

for i in range(E):
    sn, en , w = map(int, input().split())
    graph[sn].append((en,w))
    graph[en].append((sn,w))
dijkstra(1)
print(dist[N])
