import sys
input = lambda : sys.stdin.readline().strip()

s = input()
p = s[::-1]

if s == p:
    ans = 1
else:
    ans = 0

print(ans)