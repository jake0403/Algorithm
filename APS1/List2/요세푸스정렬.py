# N, k = map(int,input().split())
# num_list = [i+1 for i in range(N)]
# skip= k-1
# answer = []
# k_list = []
# for _ in range(N):
#     if skip >= len(num_list):
#         while skip >= len(num_list):
#             skip = skip - len(num_list)
#         answer.append(str(num_list.pop(skip)))
#     else:
#         answer.append(str(num_list.pop(skip)))
#     skip += k-1
#     if len(num_list) == 1:
#         break
# answer.append(str(*num_list))
# print('<',', '.join(answer)[:],'>',sep='')

#########################################################################
N, k = map(int,input().split())
num_list = [i for i in range(1,N+1)]
answer = []
skip = 0
for i in range(N):
    skip += k-1
    if skip >= len(num_list):
        # ex) skip이 4인데 num_list 개수는 2이면 skip은 num_list 개수를 나눈 나머지 값 4%2 = 0
        skip = skip%len(num_list)
    answer.append(str(num_list.pop(skip)))
print('<',', '.join(answer)[:],'>',sep='')
