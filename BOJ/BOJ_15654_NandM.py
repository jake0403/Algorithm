from itertools import permutations
L, n = map(int,input().split())
arr = list(map(int,input().split()))
result = list(permutations(arr,n))
result = [list(x) for x in result]
for i in sorted(result):
    print(*i)