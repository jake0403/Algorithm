numbers =[0,0,0,0,0,0,0,0,1]

def solution(numbers):
    result = -1
    N = len(numbers)
    max_num = max(numbers)
    if max_num == 0:
        return 0
    mN = len(bin(max_num)[2:])
    answer = []
    for i in range(N):
        binary = list(bin(numbers[i])[2:])[::-1]
        b = len(binary)
        if N > b:
            binary += [0]*(N - b)
        answer.append(binary[i])
    A = len(answer)
    answer = [int(x) for x in answer]
    if answer[0]:
        result = 1
    for i in range(1, A):
        if answer[i]:
            result+= 2**i
    return result


print(solution(numbers))