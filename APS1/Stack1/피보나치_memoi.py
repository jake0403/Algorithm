def fibo_memo(n):
    global memo
    if n >=2 and len(memo) <= n:
        memo.append(fibo_memo(n-1)+fibo_memo(n-2))
    return memo[n]
def fibo_dp(n):
    f = [2,2]
    for i in range(2,n+1):
        f.append(f[i-1] + f[i-2])
    return f

memo = [0,1]
n = 10
print(fibo_memo(n))
print(fibo_dp(n))