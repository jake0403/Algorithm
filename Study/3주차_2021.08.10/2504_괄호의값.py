import sys
input = lambda : sys.stdin.readline().strip()

palin = input()

def checkPalindorm(palin):
    check = {
        "]":"[",
        ")": "("
    }
    c_list = []
    for p in palin:
        if p  not in check:
            c_list.append(p)
        elif c_list and check[p] == "(":
            cnt = 0
            while c_list:
                end = c_list.pop()
                if end == check[p]:
                    if not cnt:
                        c_list.append(2)
                    else:
                        c_list.append(2 * cnt)
                    break
                else:
                    if end == "[":
                        return 0
                    else:
                        cnt+=end
        else:
            cnt = 0
            while c_list:
                end = c_list.pop()
                if end == check[p]:
                    if not cnt:
                        c_list.append(3)
                    else:
                        c_list.append(3 * cnt)
                    break
                else:
                    if end == "(":
                        return 0
                    else:
                        cnt+=end
    answer = 0
    for c in c_list:
        if c == '(' or c == ')' or c == '[' or c == ']':
            return 0
        else:
            answer+=c
    return answer

print(checkPalindorm(palin))