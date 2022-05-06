import sys
input = lambda : sys.stdin.readline().strip()
s = input()
t = input()
answer = 1
ls = len(s)
lt = len(t)
s = s*lt
t = t*ls
if s == t:
    print(1)
else:
    print(0)