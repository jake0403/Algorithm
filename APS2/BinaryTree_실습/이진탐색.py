def inOrder(n):
    global num, graph
    if n <= V:
        inOrder(n*2)
        graph[n] = num
        num+=1
        inOrder(n*2+1)

T = int(input())
for tc in range(1, T+1):
    V = int(input())
    graph = [0]*(V+1)
    num = 1

    inOrder(1)
    print(f'#{tc} {graph[1]} {graph[int(V/2)]}')