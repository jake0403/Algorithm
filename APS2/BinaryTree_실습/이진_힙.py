T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = list(map(int,input().split()))
    heap = [0]*(N+1)
    ans = 0
    for i in range(1, N+1):
        heap[i] = tree[i-1]

        while i > 0:
            if heap[i] < heap[i//2]:
                heap[i] , heap[i//2] = heap[i//2], heap[i]
            i//=2
    while N//2 > 0:
        ans+=heap[N//2]
        N//=2
    print(ans)