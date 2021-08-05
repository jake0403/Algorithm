import heapq
import sys
input = lambda : sys.stdin.readline().strip()
INF = sys.maxsize

N = int(input())
M = int(input())
dist = [INF]*(N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    sn, en, w = map(int, input().split())
    graph[sn].append((en, w))
start, end = map(int, input().split())
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    dist[start] = 0
    while q:
        d, now = heapq.heappop(q)
        if d > dist[now]:
            continue
        for i in graph[now]:
            cost = d + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
dijkstra(start)
print(dist[end])