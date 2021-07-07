'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(s, V):
    q = []                  # 큐 생성
    visited = [0]*(V+1)     # visitied 생성
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 시작점 처리 표시

    while q:                # 대기중인 번호가 있으면
        n = q.pop(0)        # 먼저 들어온 순서대로 꺼냄
        print(n)            # do(n)
        # 바로 뒤에 연결된 번호가 있으면 (인접 노드 중 표시 안 된 노드 i가 있으면)
        for i in range(1, V+1):
            # 대기열에 들어가지 않는다면
            if adj[n][i] and visited[i] == 0:
                q.append(i)
                visited[i] = 1 + visited[n]     # 거리 정보 입력 => + visited[n]

def bfs2(s, V):
    q = []                  # 큐 생성
    visited = [0]*(V+1)     # visitied 생성
    q.append(s)             # 시작점 인큐
    visited[s] = 1          # 시작점 처리 표시

    while q:                # 대기중인 번호가 있으면
        n = q.pop(0)        # 먼저 들어온 순서대로 꺼냄
        print(n)            # do(n)
        # 바로 뒤에 연결된 번호가 있으면 (인접 노드 중 표시 안 된 노드 i가 있으면)
        for i in adjlist[n]:
            if visited[i] == 0:  # 아직 대기중이 아니면
                q.append(i)
                visited[i] = 1 + visited[n]

V, E = map(int,input().split())
edge = list(map(int, input().split()))

adj = [[0]*(V+1) for _ in range(V+1)]   # 인접 행렬
for i in range(E):
    adj[edge[i*2]][edge[i*2+1]] = 1
    adj[edge[i*2+1]][edge[i*2]] = 1     # 무향 그래프

adjlist = [[] for _ in range(V+1)]      # 인접 리스트인 경우
for i in range(0, E*2, 2):
    adjlist[edge[i]].append(edge[i+1])
    adjlist[edge[i+1]].append(edge[i])

print(bfs(1, V))