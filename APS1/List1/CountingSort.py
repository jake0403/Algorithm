def Counting_Sort(A,B,k):
    C = [0]*(k+1)       # Counting Array (0부터 최댓값 k까지 이므로 k+1개)

    for i in range(0,len(B)):       # 0 ~ A나 B Array의 길이 만큼 반복
        C[A[i]]+=1                  # A의 Array 요소 개수 C에 담기

    for i in range(1, len(C)):      # C에 각 요소 누적 합 담기
        C[i] += C[i-1]
    print(C)
    for i in range(len(A)-1, -1, -1):       # A의 원소 값을 역순으로 담기 위해서
        B[C[A[i]]-1] = A[i]                 # B의 (A 원소 값의 C의 인덱스 - 1) =(C[A[i]) 위치에 값을 넣어준다
        C[A[i]] -= 1                        #  그 후 C 누적 값의 값을 빼준다 왜냐? B에 넣어줬으니깐!
    return B

# A  []  -- 입력 배열 (1 to k)
# B  []  -- 정렬된 배열 담을 그릇.
# C  []  -- 카운트 배열 + 누적 값.
A = [0,1,4,2,3,3,0]
B = [-1]*len(A)
k = 4
print(Counting_Sort(A,B,k))