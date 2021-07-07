def ap(n , cnt):
    global minV
    if cnt == 0:
        if minV > n:
            minV = n
    elif minV <= n:
        return
    elif 25 <= n:
        return
    else:
        for i in range(10):
            for j in range(10):
                if array[i][j] == 1 and visited[i][j] == 0:
                    for k in range(5,0,-1):



array = [list(map(int, input().split())) for _ in range(10)]
visited = [[0]*10 for _ in range(10)]
cnt_1 = 0
minV = 26
paper = [0, 5, 5, 5, 5, 5]
for a in array:
    cnt_1 += a.count(1)






