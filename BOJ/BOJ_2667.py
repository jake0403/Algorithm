from collections import deque
def bfs(i,j, street_num):
    q = deque()
    q.append([i,j])
    street[i][j] = street_num
    visited[i][j] = 1


    while q:
        i, j = q.popleft()
        for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] ==0 and street[ni][nj] != 0:
                q.append([ni,nj])
                visited[ni][nj] = 1
                street[ni][nj] = street_num

N = int(input())
street = [list(map(int,input())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
street_num = 1
for i in range(N):
    for j in range(N):
        if street[i][j] == 1 and visited[i][j] == 0:
            bfs(i,j, street_num)
            street_num+=1

# print(street)
answer = [0]*(street_num-1)
for i in street:
    for j in range(1,street_num):
        answer[j-1]+=i.count(j)

print(street_num-1)
answer.sort()
for a in answer:
    print(a)