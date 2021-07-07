T = int(input())
for tc in range(1, T+1):
    colorArr = [[0]*10 for x in range(10)]
    N = int(input())
    for i in range(N):
        color = list(map(int, input().split()))
        for r in range(color[0], color[2]+1):
            for c in range(color[1],color[3]+1):
                colorArr[r][c]+= color[4]
    count = 0
    for col in colorArr:
        for c in col:
            if c == 3:
                count+=1
    print('#{} {}'.format(tc, count))
