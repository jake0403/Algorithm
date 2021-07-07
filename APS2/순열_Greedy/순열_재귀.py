def f(i,n,k):
    if i == k:
        print(p[:k])
    else:
        for j in range(i,n):
            p[i], p[j] = p[j], p[i]
            f(i+1, n, k)
            p[i], p[j] = p[j], p[i]

N = 5
K = 2
p = [x+1 for x in range(N)]
print(f(0,N,K))