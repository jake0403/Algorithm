import sys
input = lambda : sys.stdin.readline().strip()

N, M, T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

x, d, k  = map(int, input().split())

def rotation():
    for i in range(1,N+1):
        if i % x == 0:
            pass
