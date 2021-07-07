def find_root(si):
    node[si] = 1
    for i in range(1,v+1):
        if node[i] != 1 and adj[si][i] == 1:
            find_root(i)
    return

v,e = map(int, input().split())
adj = [[0]*(v+1) for _ in range(v+1)]
for _ in range(e):
    sn, en = map(int, input().split())
    # 무방향 그래프
    adj[sn][en] = 1
    adj[en][sn] =1
node = [0]*(v+1)
cnt = 0
for i in range(1,v+1):
    if node[i] == 0:
        find_root(i)
        cnt+=1
print(cnt)