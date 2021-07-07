B_POS = []
C_NEG = []
C_NEG_Up = []
B_POS_Up = []
def solution(A):
    A.sort()
    print(A)
    for j in A:
        if j < 0:
           C_NEG.append(j)
           if (len(str(j)) == 2):
              C_NEG_Up.append(j)
        else:
            B_POS.append(j)
            if (len(str(j)) == 1):

                B_POS_Up.append(j)
    both = B_POS_Up + B_POS_Up
    print(max(both,default = None))


def solutions(A):
    # 조건에 따라 가장 작은 수 max값으로 설정
    max_one_digits = -10000
    for a in A:
        # max값이 양수이면 음수 비교할 필요 없으므로 조건 추가
        if max_one_digits < 0:
            # 음수이면서 한 자리 수인 값 찾으며 큰 값 비교
            if a < 0 and len(str(a)) == 2:
                max_one_digits = max(max_one_digits, a)

        # 양수이면서 한 자리 수인 값 찾으며 큰 값 비교
        elif a > 0 and len(str(a)) == 1:
            max_one_digits = max(max_one_digits, a)
    return max_one_digits


print(solutions([-6, -91, 1011, -100, 84, -22, 0, 1, 473]))