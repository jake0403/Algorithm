import sys
input = sys.stdin.readline

def checkCycle(sn, en):
    global num
    nn = arr[sn]
    if visited[nn]:
        num += 1
        return
    visited[nn] = 1
    checkCycle(nn, en)

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0]*(N+1)
    num = 0

    for i in range(1,N+1):
        if not visited[i]:
            visited[i] = 1
            checkCycle(i,i)
    print(num)