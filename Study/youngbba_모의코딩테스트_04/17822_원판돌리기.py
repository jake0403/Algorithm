from pprint import pprint
import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()

def rotation(x, d, k):
    k %= M
    for i in range(1,N):
        if (i+1) % x !=0:
            continue
        # 반시계 방향
        if d:
            L1, L2 = arr[i][:k], visited[i][:k]
            R1, R2 = arr[i][k:], visited[i][k:]
        # 시계 방향
        else:
            L1, L2  = arr[i][:-k], visited[i][:-k]
            R1, R2 = arr[i][-k:], visited[i][-k:]
        arr[i] = R1 + L1
        visited[i] = R2 + L2

def bfs(r,c):
    q = deque()
    q.append([r,c])
    cnt = 0
    while q:
        r,c = q.popleft()
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nr = r + dr
            nc = (c + dc) % M
            if 0<=nr<N and not visited[nr][nc] and arr[r][c] == arr[nr][nc]:
                visited[nr][nc] = 1
                q.append([nr,nc])
                cnt += 1
    return cnt





N, M, T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
total = sum([sum(x) for x in arr])
total_num = N*M
# pprint(f'첫 번째 : {arr}')
visited = [[0]*M for _ in range(N)]
for t in range(T):
    x, d, k  = map(int, input().split())
    rotation(x,d,k)
    # pprint(f'{t+1} rotation 후: {arr}')
    adj = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                remove = bfs(i,j)
                if remove:
                    adj = 1
                    total -= (arr[i][j] * remove)
                    total_num -= remove

    # if adj:
    #     pprint(f' {t+1} 인접 삭제 후: {arr} ')
    if total_num == 0:
        print(0)
        sys.exit()
    if not adj:
        avg = total / total_num
        for i in range(N):
            for j in range(M):
                if not visited[i][j]:
                    if arr[i][j] > avg:
                        arr[i][j]-=1
                        total-=1
                    elif arr[i][j] < avg:
                        arr[i][j]+=1
                        total+=1
        # pprint(f' {t+1} 인접한 것이 없을 때 : {arr}')
# print(visited)
print(total)