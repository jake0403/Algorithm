T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dock = []
    for i in range(N):
        dock.append(list(map(int, input().split())))
    dock.sort(key= lambda x: x[1])
    cnt = 1
    start = dock[0][1]
    for i in range(1,N):
        if start <= dock[i][0]:
            start = dock[i][1]
            cnt+=1
    print(cnt)