arr = [-1,3,-9,6,7,-6,1,5,4,-2]
n = len(arr)
ans = []
for i in range(1<<n):
    s = 0
    for j in range(n):
        if i & (1<<j):
            s+=arr[j]
    if s == 0:
        a = []
        for j in range(n):
            if i & (1<<j):
                a.append(arr[j])
        #print(a)
        ans.append(a)
print(ans)
from itertools import product
subset = list(product(arr, repeat=3))
subset = [x for x in subset if sum(x)==0]
print(subset)