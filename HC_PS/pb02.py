from itertools import permutations
def solution(k,m):
    result = 0
    num_permu = list(permutations(range(1,k+1), k))
    for i in range(len(num_permu)):
        num_permu[i] = [str(x) for x in num_permu[i]]
        num_permu[i] = ''.join(num_permu[i])
    for i in range(len(num_permu)):
        if int(num_permu[i]) % m == 0:
            result+=1

    return result

print(solution(5,1))
