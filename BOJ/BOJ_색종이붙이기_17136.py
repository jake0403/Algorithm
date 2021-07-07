# n : 사용한 종이 수, s : 남은 1의 수
def func(n,oc):
    global minV
    # 1의 수가 없다면
    if oc == 0:
        if n < minV:
            minV = n
    # 사용한 종이 수가 이전의 사용한 종이 수보다 크거나 같으면
    elif minV <= n:
        return
    # 사용한 종이 수가 보유한 종이 수와 같거나 크다면
    elif 25 <= n:
        return
    else:
        for i in range(10):
            for j in range(10):
                if array[i][j] == 1 and visited[i][j] == 0:
                    # 가장 큰 색종이부터 줄어들면서 확인
                    for k in range(5,0,-1):
                        # 종이가 남아 있고 그 덮은 종이가 배열을 벗어나지 않으면
                        if paper[k] > 0 and i + k <= 10 and j + k <= 10:
                            cover = 0
                            for r in range(i, i+k):
                                for c in range(j, j+k):
                                    if visited[r][c] == 0:
                                        cover += array[r][c]
                            # 색종이에 맞게 채워진다면
                            if cover == (k**2):
                                for r in range(i, i+k):
                                    for c in range(j, j+k):
                                        visited[r][c] = 1
                                paper[k]-=1
                                func(n+1, oc-(k**2))
                                # 채웠다고 끝이 아님 다른 부분도 덮지 않았을 경우
                                # 최소가 될 수 있는지 확인해야 됨.
                                # 좌측 상단 제외 방문한 곳 초기화
                                for r in range(i, i+k):
                                    for c in range(j, j+k):
                                        visited[r][c] = 0
                                paper[k] += 1
                    return


array = [list(map(int, input().split())) for _ in range(10)]
visited = [[0]*10 for _ in range(10)]
# 색종이 수 5개, 5장이므로 최대 수는 25
minV = 26
paper = [0, 5, 5, 5, 5, 5]
#  array에 있는 1의 수를 count
oc = 0
for i in range(10):
    for j in range(10):
        if array[i][j] == 1:
            oc+=1
func(0,oc)
if minV == 26:
    minV = -1
print(minV)
