def inOrder(n):
    global graph, cnt
    if n <= N:
        inOrder(n*2)
        graph[n] = cnt
        cnt+=1
        inOrder(n*2+1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    graph = [0]*(N+1)
    cnt = 1
    inOrder(1)
    print('#{} {} {}'.format(tc, graph[1], graph[int(N/2)]))
