postfix = input()
postfix = list(postfix)
stack = []
answer = ''
for i in range(len(postfix)):
    if postfix[i].isdigit():
        answer+=postfix[i]
    else:
        #닫는 괄호이면
        if postfix[i] == ")" and stack:
            while stack[-1] != "(":
                answer+=stack.pop()
        elif postfix[i] == '*' or postfix[i] == '/':
            if stack[-1] == '*' or stack[-1] == '/':
                answer+=stack.pop()
                stack.append(postfix[i])

        stack.append(postfix[i])
print(answer)
print(stack)