def factorial(N):
    if N == 0 or N ==1:
        return 1
    return N * factorial(N-1)

print(factorial(5))

def recursive_search(num_list,n,k,v):
    if n == k:
        return 0
    elif num_list[n] == v:
        return 1
    else:
        return recursive_search(num_list, n+1, k, v)


num_list = [7,2,4,3,5,8]
N = len(num_list)
v = 5
print(recursive_search(num_list,0, N, v))