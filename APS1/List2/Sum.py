def cross(num_arr):
    i = j = cross_sum = 0
    for n in range(101):
        cross_sum += num_arr[i][j]
        i+=1
        j+=1
    return cross_sum

def cross_reverse(num_arr):
    i = 0
    j = 99
    cross_sum = 0
    for n in range(101):
        cross_sum+= num_arr[i][j]
        i+=1
        j-=1
    return cross_sum


for tc in range(10):
    T = int(input())
    num_arr = [list(map(int,input().split())) for x in range(100)]
    max_num = 0
    for num in num_arr:
        print(len(num))
        if max_num < sum(num):
            max_num = sum(num)
            print(max_num)
    cross_sum = cross(num_arr)
    print('cross: ', cross_sum)
    revere_cross = cross_reverse(num_arr)
    print('reverse: ', revere_cross)
    for i in range(3):
        if max_num < cross_sum:
            max_num = cross_sum
        if max_num < revere_cross:
            max_num = revere_cross
    print(f'#{T} {max_num}')