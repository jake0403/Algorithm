import heapq

def dijkstra(start):
    q= []
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

T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    INF = 10000000
    dist = [INF]*(n+1)
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        sn, en, w = map(int, input().split())
        graph[sn].append((en, w))
    dijkstra(0)
    print(f'#{tc} {dist[n]}')