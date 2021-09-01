import sys
input = lambda : sys.stdin.readline().strip()

L, C = map(int, input().split())
words = list(input().split())
words.sort()
vowels = ['a','e','i','o','u']
cnt = 0
answer = []
word = ["" for _ in range(L)]
def passwords(idx, s, vCnt, cCnt):
    global word
    if idx == L:
        if vCnt and cCnt >= 2:
            print(''.join(map(str, word)))
        return
    for i in range(s,C):
        word[idx]=words[i]
        if words[i] in vowels:
            vCnt+=1
            passwords(idx+1, i+1, vCnt, cCnt)
            vCnt-=1
        else:
            cCnt+=1
            passwords(idx+1, i+1, vCnt, cCnt)
            cCnt-=1
passwords(0,0,0,0)