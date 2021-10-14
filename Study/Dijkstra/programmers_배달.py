import sys
import heapq
def solution(N,road, K):
    answer = 0

    INF = sys.maxsize
    graph = [[] for _ in range(N+1)]
    distance = [INF]*(N+1)

    for i in range(len(road)):
        graph[road[i][0]].append((road[i][1], road[i][2]))
        graph[road[i][1]].append((road[i][0], road[i][2]))

    def dijkstra(start):
        q = []
        heapq.heappush(q,(0, start))
        distance[start] = 0

        while q:
            dist, node = heapq.heappop(q)

            if distance[node] < dist:
                continue

            for n, d in graph[node]:
                cost = d + dist
                if cost < distance[n]:
                    distance[n] = cost
                    heapq.heappush(q, (cost, n))
    dijkstra(1)
    for i in range(1, N+1):
        if distance[i] <= K:
            answer+=1

    return answer

if __name__ == '__main__':
    N = 5
    road = [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]]
    K = 3
    print(solution(N,road,K))
    '''
    result = 4
    N = 6
    road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
    K = 4
    result = 4
    '''