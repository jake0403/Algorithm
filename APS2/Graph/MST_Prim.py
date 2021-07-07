'''
5 6
1 2 3
1 3 7
2 3 1
3 4 4
2 5 2
5 4 2
u v w
'''

V, E  = map(int, input().split())
INF = 10000     # 인접 행렬 초기 값
adj = [[INF]*(V+1) for _ in range(V+1)]

for i in range(V+1):
    adj[i][i] = 0
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u][v] = w
    adj[v][u] = w   # MST 는 무향 그래프 이므로 양방향 weight 설정

key = [INF]*(V+1)   # key[i]는 i가 MST에 연결되는 비용
key[1] = 0
MST = [0] * (V+1)
pi = [0] * (V+1)

for _ in range(V):     # 모든 정점이 MST에 포함될 때 까지
    # MST에 포함되지 않은 정점 중 key[u]가 최소인 u 값 찾기
    u = 0
    minV = INF
    for v in range(1, V+1):
        if MST[i] == 0:
            if key[v] < minV:
                u = i
                minV = key[i]

    MST[u] = 1      # key[u]가 최소인 u를 MST에 추가
    for v in range(1, V+1):     # u에 인접인 v에 대해
        if MST[v] == 0 and u != v and adj[u][v] < INF:
            if key[v] > adj[u][v]:      # 기존보다 더 작은 비용으로 MST에 연결된다면
                key[v] = adj[u][v]
                pi[v] = u       # v는 u와 연결해서 MST에 포함될 예정
print(key)