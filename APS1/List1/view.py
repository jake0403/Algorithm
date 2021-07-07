# TC  = 10
# for tc in range( 1, TC + 1):
#     N  = int(input())
#     A = list(map(int, input().split()))
#
#     cnt = 0
for test_case in range(1,11):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    #[0,0,3,5,2,4,9,0,6,4,0,6,0,0]
    num_list = list(map(int,input().split()))
    count = 0
    for i in range(2,n-2):
        max_v = 0
        for j in range(-2,3):
            if j == 0: continue
            elif max_v < num_list[i+j]:
                max_v = num_list[i+j]
        if num_list[i] > max_v:
            count+=num_list[i] - max_v
    print(f'#{test_case} {count}')