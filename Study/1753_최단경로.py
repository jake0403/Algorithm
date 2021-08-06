import heapq
import sys
input = lambda : sys.stdin.readline().strip()

N, M = map(int, input().split())
start = int(input())
INF = sys.maxsize
dist = [INF] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    sn, en, w  = map(int, input().split())
    graph[sn].append((en, w))

def shortestWay(start):
    q = []
    heapq.heappush(q,(0, start))
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
shortestWay(start)
for i in range(1,N+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])