# 반복문을 이용한 선형시간 O(N)

def Iterative_Power(x,n):
    result = 1

    for i in range(1, n+1):
        result *= x
    return result


# 분할 정복을 이용한 거듭제곱 O(logN)
def recursive_Power(x, n):
    if n ==1 : return 1
    if n%2 == 0:
        y = recursive_Power(x, n//2)
        return y**2
    else:
        y = recursive_Power(x, (n - 1)//2)
        return y**2*x