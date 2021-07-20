import sys

input = sys.stdin.readline

T, W = map(int, input().split())
plum_drop = []
for i in range(T):
    plum_drop.append(int(input()))

plum = plum_drop[::-1]
cnt = 0
for i in range(T-1):
    if plum_drop[i] != plum_drop[i+1]:
        cnt+=1
        idx = i
print(idx)
idx = T-i
left = len(plum_drop[:idx])


