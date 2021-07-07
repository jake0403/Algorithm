def f(n,k):     # n : 숫자를 채울 인덱스, k : p의 크기
    if n == k:
        print(p)
    else:
        for i in range(1, k+1):
            p[n] = i
            f(n+1, k)

N = int(input())
p = [0] * N
f(0,N)