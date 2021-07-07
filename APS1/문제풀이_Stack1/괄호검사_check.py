T = int(input())
for tc in range(1, T+1):
    check = input()
    d = {
        '}' : '{',
        ')' : '(',
    }
    stack = []
    flag = 1
    for c in check:
        if c == '(' or c == '{':
            stack.append(c)
        if c in d:
            if not stack or stack.pop() != d[c]:
                flag = 0
                break
    if stack: flag = 0

    print(f'#{tc} {flag}')