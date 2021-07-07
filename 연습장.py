# 버블 정렬
def bubbleSort(num_list):
    n = len(num_list)
    for i in range(n-1,0,-1):
        for j in range(i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list

num_list = [7,4,9,43,56,88,21,11,3,2]
# print('bubbleSort: {}'.format(bubbleSort(num_list)))

def countingSort(num_list):
    max_num = max(num_list)
    count = [0]*(max_num+1)
    index = [-1]*len(num_list)

    for i in num_list:
        count[i]+=1

    for c in range(1, len(count)):
        count[c]+= count[c-1]
    for i in range(len(num_list)-1, -1, -1):
        index[count[num_list[i]]-1] = num_list[i]
        count[num_list[i]]-=1
    return index

# print('CountingSort : {}'.format(countingSort(num_list)))
N = int(input())
a= [[0]*N for x in range(N)]
for i in range(len(a)):
    start = i
    end = len(a[0])
    for j in range(len(a[0])):
        if start < end:

            start+=1
            a[i][j] = start
        else:
            end-=1
            a[i][j] = end


for i in a:
    print(i)
# count= 1
# b = [[0]*N for x in range(N)]
# for i in range(N):
