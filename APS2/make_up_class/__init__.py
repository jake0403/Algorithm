def perm(idx, n):
    if idx == n:
        print(sel)
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                sel[i] = arr[i]
                perm(i+1,n)
                visited[i] = 0

arr = [x for x in range(1, 5+1)]
N = len(arr)
sel = [0]*N
visited = [0]*N
print(perm(0,N))