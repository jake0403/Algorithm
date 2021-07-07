def dijkstra(s,V,D, adj):
    U = [0]*(V+1)
    U[s] = 1
    for v in range(V+1):
        D[v] = adj[s][v]

    for _ in range(V):
        minV = INF
        w = 0
        for i in range(V+1):
            if U[i] == 0 and minV > D[i]:
                minV = D[i]
                w = i
        U[w] = 1
        for v in range(V+1):
            if 0< adj[w][v] < INF:
                D[v] = min(D[v], D[w] + adj[w][v])

T = int(input())
for tc in range(1, T+1):
    V, E, targetH = map(int, input().split())
    INF = 1000000
    # 파티로 향하는 인접행렬
    adjF = [[INF]*(V+1) for _ in range(V+1)]
    # 파티에서 집으로 되돌아가는 인접행렬
    adjT = [[INF]*(V+1) for _ in range(V+1)]
    for i in range(1,V+1):
        adjF[i][i] = 0
        adjT[i][i] = 0
    for _ in range(E):
        u,v,w = map(int, input().split())
        adjF[u][v] = w
        adjT[v][u] = w

    D1 = [0]*(V+1)
    D2 = [0]*(V+1)
    dijkstra(targetH, V, D1, adjF)
    dijkstra(targetH, V, D2, adjT)

    maxL = 0
    for i in range(1,V+1):
        if D1[i] + D2[i] > maxL:
            maxL = D1[i]+ D2[i]
    print(f'#{tc} {maxL}')

