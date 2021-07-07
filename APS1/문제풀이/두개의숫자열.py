T = int(input())
for tc in range(1, T+1):
    A,B = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    # A는 짧은 Array B는 긴 Array로 지정
    if A > B:
        A ,B = B, A
        a_list, b_list = b_list, a_list
    tmp = 0
    max_num = -987654321
    # 긴 Array에 짧은 Array 비교하는 것이니 (긴 거 - 짧은 거 +1)
    for i in range(B-A+1):
        tmp = 0
        for j in range(len(a_list)):
            # 바보같이 list 하나 더 생성해서 slicing 함...
            # tmp += B[i+j]*A[j] => 이렇게 해주는 게 메모리를 더 안 잡아먹음 ㅠㅠ
            sl = b_list[i:len(a_list)+i]
            tmp += sl[j]*a_list[j]
        # 최댓값 구하기
        if max_num < tmp:
            max_num = tmp
    print(f'#{tc} {max_num}')



#######################################################################################################################

Test = int(input())

def check(long, short):
    max_value = -987654321
    for i in range(len(long) - len(short)+1):
        result = 0
        for j in range(len(short)):
            result+= long[i+j]*short[j]
    if max_value < result:
        max_value = result
    return max_value

for tc in range( 1, Test+1):
    N, M = map(int, input().split())

    A = list(map(int, input()))
    B = list(map(int, input()))
    if N > M :
        ans = check((A,B))
    else:
        ans = check((B,A))
