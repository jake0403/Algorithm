def inOrder(idx):
    global result
    if idx > n:
        return
    inOrder(2*idx)
    result+=arr[idx]
    inOrder(2*idx+1)


for tc in range(1,11):
    n = int(input())
    arr = [0]*(n+1)
    result = ''
    for i in range(n):
        a = list(input().split())
        arr[int(a[0])] = a[1]
    inOrder(1)
    print(f'#{tc} {result}')
