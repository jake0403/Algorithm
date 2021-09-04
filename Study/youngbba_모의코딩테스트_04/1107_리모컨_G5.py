import sys
input = lambda : sys.stdin.readline().strip()

N = int(input())
M = int(input())
broken = input().split()
ans = 0
start = 100
if start == int(N):
    print(ans)
    sys.exit()
ans = abs(N - start)

for btn in range(1000000):
    for i in range(len(str(btn))):
        if str(btn)[i] in broken:
            break
        elif i == len(str(btn))-1:
            ans = min(ans, abs(btn - N) + len(str(btn)))
print(ans)