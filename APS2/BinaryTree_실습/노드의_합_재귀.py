def postOrder(n):
    global tree
    if n > N:
        return 0
    if tree[n] > 0:
        return tree[n]
    tree[n] = postOrder(n*2) + postOrder(n*2+1)
    return tree[n]
T = int(input())
for tc in range(1, T+1):
    N, M ,L = map(int, input().split())
    tree = [0]*(N+1)
    for _ in range(M):
        n, v = map(int, input().split())
        tree[n] = v

    postOrder(L)
    print(f'#{tc} {tree[L]}')
