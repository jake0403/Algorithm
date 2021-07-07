T = int(input())
def operator(n1,n2, o):
    if o == '+':
        return n1 + n2
    elif o == '-':
        return n1 - n2
    elif o == '*':
        return n1 * n2
    else:
        return n1//n2


for tc in range(1, T+1):
    forth = list(input().split())
    stack =[]
    answer = 0
    for f in forth:
        if f.isdigit():
            stack.append(int(f))
        else:
            if f == '.':
                if len(stack) != 1:
                    answer = 'error'
            else:
                if len(stack) >= 2:
                    num1, num2 = stack.pop(), stack.pop()
                    answer = operator(num1,num2, f)
                    stack.append(answer)
                else:
                    answer = 'error'
                    break
    if len(stack) and type(answer) != str:
        answer = stack[0]
    print(f'#{tc} {answer}')