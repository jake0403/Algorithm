import sys
input = lambda : sys.stdin.readline().strip()

palin = list(input())
check_dict = {
    ')' : '(',
    ']' : '['
}
def check(p):
    N = len(p)
    stack = []
    for i in range(N):
        if p[i] in check_dict:
            if not stack:
                return 0
            c = stack.pop()
            if c != check_dict[p[i]]:
                return 0
        else:
            stack.append(p[i])
    if stack:
        return 0
    return 1

def calc(p):
    stack = []
    N = len(p)
    for i in range(N):
        if p[i] == ']':
            if stack[-1] == check_dict[p[i]]:
                stack[-1] = 3
            else:
                tmp = 0
                for r in range(len(stack)-1,-1,-1):
                    if stack[r] == check_dict[p[i]]:
                        stack[-1] = tmp * 3
                        break
                    else:
                        tmp += stack.pop()
        elif p[i] == ')':
            if stack[-1] == check_dict[p[i]]:
                stack[-1] = 2
            else:
                tmp = 0
                for r in range(len(stack)-1, -1, -1):
                    if stack[r] == check_dict[p[i]]:
                        stack[-1] = tmp * 2
                        break
                    else:
                        tmp += stack.pop()
        else:
            stack.append(p[i])
    return sum(stack)

if not check(palin):
    print(0)
else:
    print(calc(palin))