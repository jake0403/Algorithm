from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()

K = int(input())
M,N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 말 움직임 횟수 체크 위해 3차원 배열로 방문+이동 횟수 체크
visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
# 말 움직임
km = ([-2,1],[-1,2],[2,1],[1,2],[1,-2],[2,-1],[-1,-2],[-2,-1])
# 원숭이 움직임
mm = ([0,1],[1,0],[-1,0],[0,-1])
def bfs():
    q = deque()
    q.append([0,0,0])
    # 우선 start 부분 1로 초기화
    visited[0][0][0] = 1
    def monkey(r,c,z):
        for dr, dc in mm:
            nr, nc = r + dr, c + dc
            if 0<= nr < N and 0<= nc < M:
                if arr[nr][nc] == 0 and visited[nr][nc][z] == 0:
                    # 원숭이 움직임은 말 움직임과 상관 없으므로 z 안 더함
                    visited[nr][nc][z] = visited[r][c][z]+1
                    q.append([nr,nc,z])
    def knight(r,c,z):
        for dr, dc in km:
            nr, nc = r+dr, c+dc
            if 0<= nr < N and 0<= nc <M:
                if arr[nr][nc] ==0 and visited[nr][nc][z+1] == 0:
                    visited[nr][nc][z+1] = visited[r][c][z]+1
                    q.append([nr,nc,z+1])

    while q:
        r,c,z = q.popleft()
        if r == N-1 and c == M-1:
            # visited start를 1로 해줬기 떄문
            answer = visited[r][c][z]- 1
            return answer
        if z < K:
            monkey(r,c,z)
            knight(r,c,z)
        else:
            monkey(r,c,z)
    return -1

print(bfs())