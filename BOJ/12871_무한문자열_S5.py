import sys
input = lambda : sys.stdin.readline().strip()

s = input()
t = input()
if len(s) > len(t):
    s, t = t, s
m = len(t)
n = len(s)
flag = 1
for i in range(m, n, n):
    if t[m-n:i] != s:
        flag = 0
print(flag)