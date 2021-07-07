
N = int(input())
num_list = list(map(int, input().split()))

max_h = 0
for i in range(N-1):
    count = 0
    for j in range(i+1, N):
        if num_list[i] > num_list[j]:
            count+=1

        if max_h < count :
            max_h = count
print(max_h)