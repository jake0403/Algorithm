def forth_true(forth):
    stack = []
    def calculate(c, a, b):
        if c == '+':
            return a + b
        elif c == '-':
            return a - b
        elif c == '*':
            return a * b
        else:
            return a // b
    for f in forth:
        # 연산자가 . 이라면
        if f == '.':
            if len(stack) == 1:
                answer = stack[0]
                return answer
            else:
                return 'error'
        # 숫자라면 stack에 추가
        elif f.isdigit():
            stack.append(int(f))
        # stack에 숫자가 두 개 미만인데 'f'가 연산자라면
        elif len(stack) < 2 and not f.isdigit():
            return "error"
        # 연산자라면 스택에서 피연산자 두 개 꺼내고
        # 계산한 값 스택에 다시 추가
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(calculate(f,a,b))


T = int(input())
for tc in range(1, T+1):
    forth = input().split()
    print(f'#{tc} {forth_true(forth)}')