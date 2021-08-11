import sys
input = lambda : sys.stdin.readline().strip()

N = int(input())
arr = sorted(list(map(int, input().split())))
answer = 0
if N % 2 == 0:
    answer = arr[N//2 - 1]
else:
    answer = arr[N//2]
print(answer)