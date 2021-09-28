import sys
input = lambda : sys.stdin.readline().strip()
N = int(input())
arr = [float(input()) for _ in range(N)]
for n in range(1,N):
    arr[n] = max(arr[n], arr[n]*arr[n-1])
print("{:.3f}".format(max(arr)))
