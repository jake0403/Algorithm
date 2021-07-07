from collections import deque
dr = [1,-1,0,0,0,0]
dc = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
def vaccine(q):
    while q:
        z,r,c = q.popleft()
        visited[z][r][c] = 1
        for i in range(6):
            nz, nr, nc = z + dz[i], r + dr[i], c + dc[i]
            if 0<=nz<h and 0<=nr<n and 0<=nc<m and apartment[nz][nr][nc] == -1 and visited[nz][nr][nc] == 0:
                q.append([nz,nr,nc])
                apartment[nz][nr][nc] = apartment[z][r][c]+1
                visited[nz][nr][nc] = 1

def find_zombies():
    for i in range(h):
        for j in range(n):
            if -1 in apartment[i][j]:
                return 1
    return 0

def solution():
    zombie_cnt = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if apartment[i][j][k] == 1:
                    q.append([i,j,k])
                elif apartment[i][j][k] == -1:
                    zombie_cnt+=1
    if zombie_cnt == 0:
        answer = 'ALL HUMANS'
        return answer
    max_date = 0
    vaccine(q)
    if find_zombies():
        answer = 'STILL ZOMBIES'
        return answer
    else:
        for i in range(h):
            for j in range(n):
                max_date = max(max_date, max(apartment[i][j]))
        answer = max_date-1
        return answer

T = int(input())
for tc in range(1,T+1):
    m,n,h = map(int, input().split())
    visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
    apartment = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
    q = deque()
    print(solution())
