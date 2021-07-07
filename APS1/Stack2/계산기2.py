def postfix(S):
    stack_num = []
    stack_calc = []
    for i in S:
        # 숫자일 경우는 숫자 스택에 추가
        if i.isdigit():
            stack_num.append(i)
        else:
            # 곱하기면 숫자 두 개 무조건 있어서 두 개 곱한 값을 스택 num에 추가
            if i == '*':
                A = int(stack_num.pop())
                B = int(stack_num.pop())
                stack_num.append(A*B)
            # 덧셈이면 숫자 두 개 뽑아서 더함
            else:
                A  = int(stack_num.pop())
                B  = int(stack_num.pop())
                stack_num.append(A+B)
    return stack_num[0]

T = 10
for tc in range(1, T+1):
    N = int(input())
    calc = input()
    calc = list(calc)
    answer = ''
    stack = []
    for i in range(N):
        # 피연산자일 경우
        if calc[i].isdigit():
            answer+=calc[i]
        # 연산자일 경우
        else:
            #스택이 없는 경우에는 그냥 추가
            if not stack:
                stack.append(calc[i])
            else:
                # + 가 나오면 스택 안에 있는 연산자 answer 변수에 붙이기
                if calc[i] == '+':
                    while stack:
                        answer+=stack.pop()
                    stack.append(calc[i])
                # * 가 나오면 그냥 스택에 추가
                else:
                    stack.append(calc[i])
    # 스택에 남아 있는 연산자가 있는 경우
    if stack:
        while stack:
            answer+=stack.pop()
    print(f'{tc} {postfix(answer)}')