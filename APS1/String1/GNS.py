T = int(input())
def countingSort(A,B,k):
    C = [0]*(k+1)       # Counting Array (0부터 최댓값 k까지 이므로 k+1개)

    for i in range(0,len(B)):       # 0 ~ A나 B Array의 길이 만큼 반복
        C[A[i]]+=1                  # A의 Array 요소 개수 C에 담기

    for i in range(1, len(C)):      # C에 각 요소 누적 합 담기
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):       # A의 원소 값을 역순으로 담기 위해서
        B[C[A[i]]-1] = A[i]                 # B의 (A 원소 값의 C의 인덱스 - 1) =(C[A[i]) 위치에 값을 넣어준다
        C[A[i]] -= 1                        #  그 후 C 누적 값의 값을 빼준다 왜냐? B에 넣어줬으니깐!
    return B
for tc in range(1, T+1):

    t, N = input().split()
    N = int(N)
    num_dict = {
        'ZRO': 0,
        'ONE': 1,
        'TWO': 2,
        'THR': 3,
        'FOR': 4,
        'FIV': 5,
        'SIX': 6,
        'SVN': 7,
        'EGT': 8,
        'NIN': 9,
    }
    alphaNum = input().split()
    for i in range(N):
        alphaNum[i] = num_dict[alphaNum[i]]
    max_num = -1
    for a in alphaNum:
        if max_num < a:
            max_num = a
    # 카운팅 정렬로 정렬
    B = [-1]*N
    numAlpha = countingSort(alphaNum, B, max_num )
    # 위 딕셔너리 키 값 value 값 바꾸기
    alpha_dict = {v:k for k, v in num_dict.items()}

    for j in range(N):
        numAlpha[j] = alpha_dict[numAlpha[j]]
    numAlpha = ' '.join(numAlpha)
    print('#{}'.format(tc))
    print('{}'.format(numAlpha))




