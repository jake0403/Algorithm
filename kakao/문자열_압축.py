def solution(s):
    result = ''
    str_list = []
    if len(s) == 1:
        return 1

    for cut in range(1, len(s)//2+1):
        cnt = 1
        tmp = s[:cut]
        for i in range(cut, len(s), cut):
            if s[i:i+cut] == tmp:
                cnt +=1
            else:
                if cnt == 1:
                    cnt = ''
                result+= str(cnt)+tmp
                tmp = s[i:i+cut]
                cnt = 1
        if cnt == 1:
            cnt = ''
        result+=str(cnt)+tmp
        str_list.append(len(result))
        result = ''

    return min(str_list)