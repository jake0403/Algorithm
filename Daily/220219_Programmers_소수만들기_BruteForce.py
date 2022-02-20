from itertools import combinations
def solution(nums):
    answer = 0
    n_list = list(combinations(nums, 3))
    print(list(n_list))
    s_list = [sum(x) for x in n_list]
    print(s_list)
    def check_prime(n):
        if n<=1:
            return 0
        for i in range(2, n//2+1):
            if n % i == 0:
                return 0
        return 1

    for s in s_list:
        answer += check_prime(s)
    return answer

nums = [1,2,3,4]
print(solution(nums))