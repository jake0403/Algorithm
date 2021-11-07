import sys

input = lambda : sys.stdin.readline().strip()

na, nb = map(int, input().split())
a = list(input().split())
b = list(input().split())
arr = a+b
arr.sort()
print(*arr)
