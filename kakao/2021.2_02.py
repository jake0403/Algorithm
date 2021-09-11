import math
def solution(n, k):
    answer = 0
    def findPrime(x):
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True

    def convert(num, b):
        conv = ''
        while num > 0:
            num, mod = divmod(num, b)
            conv += str(mod)
        return conv[::-1]
    n = convert(n,k)
    print(n)
    check_list = n.split('0')
    check_list = [x for x in check_list if x and int(x)>1]
    print(check_list)
    for check in check_list:
        if findPrime(int(check)):
            answer+=1
    return answer

print(solution(110011, 10))