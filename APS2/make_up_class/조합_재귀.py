def comb(i,s,n,r):
    if i == r:
        print(c)
    else:
        for j in range(s, n-r+i+1):
            c[i] = arr[j]
            comb(i+1, j+1, n, r)
n = 3
r = 1
arr = [1,2,3]
c = [0]*r
print(comb(0,0,n,r))