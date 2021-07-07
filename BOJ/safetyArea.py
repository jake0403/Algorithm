from collections import deque
import copy
def bfs(i, j):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1

    while q:
        i, j = q.popleft()
        for di, dj in [(0,1), (1,0), (-1,0), (0,-1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and cp[ni][nj] != 0 :
                visited[ni][nj] = 1
                q.append([ni,nj])

def check(num):
    for i in range(N):
        for j in range(N):
            # 침수지역 확인
            if cp[i][j] <= num:
                cp[i][j] = 0

N = int(input())
land = [list(map(int,input().split())) for _ in range(N)]
max_num = 0
safety = 0
for i in land:
    mi = max(i)
    max_num = max(max_num, mi)
# 제일 높은 지역은 확인할 필요 X
max_num-=1

while max_num >= 0:
    cp = copy.deepcopy(land)
    visited = [[0]*N for _ in range(N)]
    cnt = 0
    check(max_num)
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and cp[i][j] !=0:
                bfs(i,j)
                cnt+=1
    safety = max(safety, cnt)
    max_num-=1
print(safety)