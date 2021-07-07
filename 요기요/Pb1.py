C = 'Example'
S = 'John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker'

from copy import deepcopy

def solution(S,C):
    # 회사명 소문자
    C = C.lower()
    # 이름 전처리
    string = S.split(';')
    S = deepcopy(string)
    string = [i.replace('-','').lower().split() for i in string]
    n = len(string)
    for i in range(n):
        if len(string[i])>2:
            if len(string[i][2]) > 8:
                string[i][2] = string[i][2][:8]
            string[i] = [string[i][0],string[i][2]]
    # [['john', 'doe'], ['peter', 'parker'], ['mary', 'watsonpa'], ['john', 'doe'], ['john', 'doe'], ['jane', 'doe'], ['peter', 'parker']]
    for i in range(n-1):
        cnt = 0
        for j in range(i+1,n):
            if string[i] == string[j]:
                cnt+=1
                string[j][1]+=str(cnt)

    answer = ''
    for i in range(n):
        answer+=f'{S[i]} <{string[i][0]}.{string[i][1]}@{C}.com>;'
        #answer+='{} <{}.{}@{}.com>;'.format(S[i], string[i][0], string[i][1],C)
        answer.rstrip()
    answer = answer[:-1]


    return answer


print(solution(S,C))




a='John Doe <john.doe@example.com>; Peter Benjamin Parker <peter.parker@example.com>; Mary Jane Watson-Parker <mary.watsonpa@example.com>; John Elvis Doe <john.doe2@example.com>; John Evan Doe <john.doe3@example.com>; Jane Doe <jane.doe@example.com>; Peter Brian Parker <peter.parker2@example.com>'