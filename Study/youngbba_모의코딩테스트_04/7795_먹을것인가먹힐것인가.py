import sys
input = lambda : sys.stdin.readline().strip()

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))
    B.sort()
    cnt = 0
    for i in range(N):
        for j in range(M):
            if A[i] > B[j]:
                cnt+=1
            else:
                break
    print(cnt)