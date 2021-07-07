#N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법
def findMax(num_list):
    max_num = -1
    for i in num_list:
        if max_num < i:
            max_num = i
    return max_num
def findMin(num_list):
    min_num = 101
    for i in num_list:
        if min_num > i:
            min_num = i
    return min_num
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int,input().split()))
    answer = []
    for i in range(10):
        if i%2 ==0:
            max_num = findMax(num_list)
            answer.append(max_num)
            num_list.remove(max_num)
        else:
            min_num = findMin(num_list)
            answer.append(min_num)
            num_list.remove(min_num)
    answer = [str(i) for i in answer]
    answer = ', '.join(answer)
    print('#{} {}'.format(tc, answer))

