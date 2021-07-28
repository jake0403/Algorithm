T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]
    for i in range(N):
        info = list(map(int, input().split()))
        color = info[-1]
        info = info[:-1]
        cnt = 0
        for i in range(info[0],info[2]+1):
            for j in range(info[1], info[3]+1):
                if not arr[i][j]:
                    arr[i][j] = color
                elif arr[i][j] and arr[i][j] != color:
                    arr[i][j] = 3
    for i in range(10):
        cnt+= arr[i].count(3)


    print(f'#{tc} {cnt}')