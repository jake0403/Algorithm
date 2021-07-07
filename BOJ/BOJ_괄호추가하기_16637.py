# i = index, s = 이전 연산값, ex = 수식
def find_Max(i, s, N, ex):
    global max_V
    if i >= N:
        if max_V < s:
            max_V = s
    else:
        # ex[i-1]은 연산자 ex[i]는 피연산자
        # 이전 연산 값과 현재 값(ex[i])을 연산자인 ex[i-1]로 연산
        t = cal(s, int(ex[i]), ex[i-1])
        # 재귀로 그 뒤 값을 계산해 최대 값 찾기
        find_Max(i+2, t, N, ex)
        # i 값이 마지막 피연산자가 아닐 경우
        if i+2 < N:
            t = cal(s, cal(int(ex[i]), int(ex[i+2]), ex[i+1]), ex[i-1])
            find_Max(i+4, t, N, ex)

def cal(i, j, op):
    if op == '+':
        return i + j
    elif op == '*':
        return i * j
    elif op == '-':
        return i - j

N = int(input())
ex = input()
max_V = -(2**31)
find_Max(2, int(ex[0]), N, ex)
print(max_V)