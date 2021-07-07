def preOrder(N):
    global cnt
    if N > 0 :
        cnt+=1
        preOrder(ch1[N])
        preOrder(ch2[N])


T = int(input())
for tc in range(1, T+1):
    E , N = map(int, input().split())
    graph = list(map(int, input().split()))
    ch1 = [0]*(E+2)
    ch2 = [0]*(E+2)
    cnt = 0
    for i in range(1, len(graph)+1, 2):
        if ch1[graph[i-1]] == 0:
            ch1[graph[i-1]] = graph[i]
        else:
            ch2[graph[i-1]] = graph[i]

    preOrder(N)
    print(f'#{tc} {cnt}')

