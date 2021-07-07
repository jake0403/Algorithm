def preOrder(n):
    global count
    if n > 0:
        count+=1
        preOrder(ch1[n])
        preOrder(ch2[n])

T = int(input())
for tc in range(1,T+1):
    E, N = map(int,input().split())
    ch1 = [0]*(E+2)
    ch2 = [0]*(E+2)
    graph = list(map(int,input().split()))
    count = 0

    for i in range(0,len(graph),2):
        if not ch1[graph[i]]:
            ch1[graph[i]] = graph[i+1]
        else:
            ch2[graph[i]] = graph[i+1]

    preOrder(N)
    print(count)