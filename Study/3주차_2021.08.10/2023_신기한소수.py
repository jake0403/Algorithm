import math

N = int(input())
prime = (2,3,5,7)

def checkPrime(num):
    if num == 0 or num == 1:
        return False
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def dfs(num, n):
    if n == N:
        print(num)
        return
    for i in range(1,10,2):
        if checkPrime(num*10+i):
            dfs(num*10+i, n+1)

for p in prime:
    dfs(p,1)