# 투포인터 함수 생성 -> 왼쪽 오른쪽을 늘려가며 회문 판별
def twoPointer(s,left, right):
    while left >=0 and right <= len(s) and s[left] == s[right-1]:
        left-=1
        right+=1
    return s[left+1: right-1]

for _ in range(10):
    tc = int(input())
    word_array = [list(input()) for _ in range(100)]
    result = ''
    # 총 길이인 100번 반복
    for i in range(100):
        s1 = ''  # 가로 단어 입력 받을 변수 생성
        s2 = ''  # 세로 단어 입력 받을 변수 생성
        for j in range(100):
            s1+=word_array[i][j]
            s2+=word_array[j][i]
        # 99번 반복 이유는 전체 s1, s2 길이 100이고
        # 전체 문자열(s1,s2)과 회문(k+1, k+2)를 비교하기 때문에 (전체 - 2=>(k+1, k+2) + 1)
        for k in range(99):
            # 큰 값 구하기 위해 그냥 max 씀....
            result = max(result,
                         twoPointer(s1,k,k+1),
                         twoPointer(s1,k,k+2),
                         twoPointer(s2,k,k+1),
                         twoPointer(s2,k,k+2),
                         key = len)
    print(f'{tc} {len(result)}')