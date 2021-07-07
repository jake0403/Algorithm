## 비트 연산으로 부분 집합 구하기
a = [1,2,3]
n = len(a)

def bitSubset(n, arr):
    ans = []
    for i in range(1<<n):
        res = []
        for j in range(n):
            if i & (1<<j):
                if arr[j]:
                    res.append(arr[j])
        ans.append(res)
    return ans

print(bitSubset(n,a)[1:])

def perm(i, n):
    if i == n:
        pass

from itertools import product, permutations, combinations
mylist = [1,2,3]
result = product(mylist, repeat=2)
answer = permutations(mylist)
ans = combinations(mylist,2)
print(list(result))
print(list(answer))
print(list(ans))
